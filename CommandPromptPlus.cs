using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Principal;
using System.Text;
using System.Threading.Tasks;

namespace CommandPromptPlus
{
    internal class CommandPromptPlus
    {
        public static bool isbeta = true;
        static void Main(string[] args)
        {
            Console.WriteLine("Better Command Prompt (Basic Utilities Extension)");
            Console.WriteLine("***************** Version 3.0.8 *****************");
            if (Utilities.sutils.IsAdministrator())
            {
                Console.BackgroundColor= ConsoleColor.DarkRed;
                Console.WriteLine("Currently running as Administrator, be careful");
                Console.ResetColor();
            }
            if (isbeta)
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("Caution: You are running beta software. Be sure to report any bug.");
                Console.ResetColor();
            }
            Console.WriteLine("\n");
            try
            { mainloop(args); }
            catch (Exception e) {
                Console.Clear();
                Console.BackgroundColor = ConsoleColor.DarkBlue;
                for (int i = 0; i < Console.WindowHeight;i++)
                {
                    Console.Write(new string(' ', Console.WindowWidth));
                }
                Console.SetCursorPosition(0, 0);
                Console.WriteLine(":(\nWe're sorry, but a fatal error occured in Command Prompt Plus.");
                Console.WriteLine("\n" +
                    "\n" +
                    $"Type: {e.GetType().Name}\n" +
                    $"Message: {e.Message}\n" +
                    $"Stack Trace: {e.StackTrace}");
                Console.WriteLine("\n\nPlease report this full message to Enderbyte Programs");
                Console.Write("Press enter to quit.");
                Console.ReadLine();
            }
        }
        static void mainloop(string[] args)
        {
            
            int hindex = 0;
            while (true)
            {
                string mcommand = "";
                Console.Write(Environment.CurrentDirectory + "> ");
                int crow = Console.CursorTop;
                int blln = Environment.CurrentDirectory.Length + 2;
                int tblxlen = 0;
                while (true)
                {
                    List<string> localhistory = Commands.shared.history;
                    ConsoleKeyInfo cki = Console.ReadKey(true);
                    if (char.IsLetterOrDigit(cki.KeyChar) || char.IsWhiteSpace(cki.KeyChar) || char.IsSymbol(cki.KeyChar) || char.IsWhiteSpace(cki.KeyChar) || "!@#%&()-_/.,;':\"][{}".Contains(cki.KeyChar))
                    { mcommand = mcommand + cki.KeyChar; }
                     if (cki.Key == ConsoleKey.Backspace)
                    {
                        if (mcommand.Length > 0)
                        { mcommand = mcommand.Remove(mcommand.Length- 1); }
                    } if (cki.Key == ConsoleKey.Enter)
                    {
                        break;
                    } if (cki.Key == ConsoleKey.UpArrow) {
                        
                        hindex++;
                        if (Commands.shared.history.Count - hindex < 0)
                        {
                            hindex--;
                        }
                        else
                        { mcommand = Commands.shared.history[localhistory.Count - hindex]; 
                        
                        }

                    } if (cki.Key == ConsoleKey.DownArrow)
                    {
                        hindex--;
                        if (hindex < 1)
                        {
                            mcommand = "";
                            hindex++;

                        } else
                        {
                            try
                            {

                                mcommand = Commands.shared.history[localhistory.Count-hindex];

                            }
                            catch (ArgumentOutOfRangeException)
                            {
                                mcommand = "";
                                hindex++;
                            }
                        }
                    }
                    tblxlen = mcommand.Length + 3;
                    Console.SetCursorPosition(blln, crow);
                    Console.Write(new string(' ', tblxlen));
                    Console.SetCursorPosition(blln, crow);
                    Console.Write(mcommand);
                    
                }
                hindex = 0;
                if (mcommand.Length > 2)
                { Commands.shared.history.Add(mcommand.Replace("\n","").Replace("\r","")); }
                Console.WriteLine("");
                DateTime start = DateTime.Now;
                int retcode = Master.interpret(mcommand.Replace("\n", "").Replace("\r", ""));
                DateTime end = DateTime.Now;
                TimeSpan diff = (end - start);
                
                if (retcode != -10000)
                {
                    Console.Write($"{diff.ToString("G")} ");
                    if (retcode != 0)
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.Write(":( ");
                        Console.Write(retcode.ToString());
                        Console.ResetColor();
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.Write(":)");
                        Console.ResetColor();
                    }
                    
                }
                Console.WriteLine("");
            }

        }
    }
    public static class Master
    {
        public static int interpret(string data)
        {
            if (data.Replace(" ","").Length == 0)
            {
                return -10000;
            }
            string[] xdata = Utilities.ParseArgs.SplitCommandLine(data).ToArray();
            string croot = xdata[0];
            string[] largs = new string[xdata.Length - 1];
            Array.Copy(xdata,1, largs, 0, xdata.Length - 1);

            if (croot.Equals("exit"))
            {
                Commands.StaticCommands.Exit(largs);
            } 
            else if (croot.Equals("about"))
            {
                Commands.StaticCommands.About(largs);
            }
            else if (croot.Equals("help"))
            {
                Commands.StaticCommands.Help(largs);
            } else if (croot.Equals("amiadmin"))
            {
                bool isadmin = Utilities.sutils.IsAdministrator();
                if (isadmin)
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("You are an administrator!");
                    Console.ResetColor();
                }
            } else if (croot.Equals("crash"))
            {
                throw new SystemException("Manual Crash");
            }
            else
            {
                Console.WriteLine("Command not found");
                return 9009;
            }

            return 0;
        }
    }
    namespace Commands
    {
        public static class shared
        {
            public static List<string> history = new List<string>();
        }
        public static class StaticCommands
        {
            public static void Exit(string[] args)
            {
                if (args.Length > 0)
                {
                    try
                    { Environment.ExitCode = Convert.ToInt16((string)args[0]); }
                    catch (Exception)
                    {

                    }
                }
                Environment.Exit(Environment.ExitCode);
            }
            public static void About(string[] args)
            {
                Console.WriteLine("=====Command Prompt Plus=====\n" + "The Better Command Prompt\n" + "(Basic Utilities fork)\n" + "\n" + "Version 3.0.8 (c) 2021-2023 Enderbyte Programs. All rights reserved\n" + "\n" + "Credits : \n" + "Developer: Jordan Rahim\n" + "That is all\n\n" + "Information: \n" + "Coded in .NET Framework 4.8 for Microsoft Windows\n" + "C# (of course)" + "\n" + "255 Lines of code\n\n" + "If you find a bug or have an issue, please report it to Enderbyte Programs immediatly." + "");
            }
            public static void Help(string[] args)
            {
                Console.WriteLine("Basic Utilities Help Menu\n" +
                    "Version 3.0.8\n" +
                    "Commands List:\n" +
                    "help: Show this menu\n" +
                    "exit [code]: Exit with optional exit code\n" +
                    "about: View some info about this program");
            }
        }

    }
    namespace Utilities
    {
        public static class sutils
        {
            public static bool IsAdministrator()
            {
                var identity = WindowsIdentity.GetCurrent();
                var principal = new WindowsPrincipal(identity);
                return principal.IsInRole(WindowsBuiltInRole.Administrator);
            }
            public static int gmaxlcount(string[] indata)
            {
                int result = 0;
                foreach (string s in indata)
                {
                    if (s.Length > result)
                    {
                        result = s.Length;
                    }
                }
                return result;
            }
        }
        public static class ParseArgs
        {
            public static IEnumerable<string> SplitCommandLine(string commandLine)
            {
                bool inQuotes = false;

                return commandLine.Split(c =>
                {
                    if (c == '\"')
                        inQuotes = !inQuotes;

                    return !inQuotes && c == ' ';
                })
                                  .Select(arg => arg.Trim().TrimMatchingQuotes('\"'))
                                  .Where(arg => !string.IsNullOrEmpty(arg));
            }
            public static IEnumerable<string> Split(this string str,
                                            Func<char, bool> controller)
            {
                int nextPiece = 0;

                for (int c = 0; c < str.Length; c++)
                {
                    if (controller(str[c]))
                    {
                        yield return str.Substring(nextPiece, c - nextPiece);
                        nextPiece = c + 1;
                    }
                }

                yield return str.Substring(nextPiece);
            }
            public static string TrimMatchingQuotes(this string input, char quote)
            {
                if ((input.Length >= 2) &&
                    (input[0] == quote) && (input[input.Length - 1] == quote))
                    return input.Substring(1, input.Length - 2);

                return input;
            }

        }
    }
}

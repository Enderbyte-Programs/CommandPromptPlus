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
        static void Main(string[] args)
        {
            Console.WriteLine("Better Command Prompt (Basic Utilities Extension)");
            Console.WriteLine("*************Version 3.0.7  BETA*****************");
            if (Utilities.sutils.IsAdministrator())
            {
                Console.BackgroundColor= ConsoleColor.Green;
                Console.WriteLine("Currently running as Administrator, be careful");
                Console.ResetColor();
            }
            Console.WriteLine("\n");
            mainloop(args);
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
                if (mcommand.Length > 0)
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
            } else
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

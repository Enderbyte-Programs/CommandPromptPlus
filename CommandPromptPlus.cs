using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Principal;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CommandPromptPlus
{
    internal class CommandPromptPlus
    {
        public static int VID = 251;
        public static bool isbeta = true;
        static void Main(string[] args)
        {
            if (!(args.Contains("-c") || args.Contains("-np")))
            {
                Console.WriteLine("Better Command Prompt (Basic Utilities Extension)");
                Console.WriteLine($"*********** Version 3.0.10 (VID {VID}) ***********");
                if (Utilities.sutils.IsAdministrator())
                {
                    Console.BackgroundColor = ConsoleColor.DarkRed;
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
            }
            try
            { mainloop(args); }
            catch (Exception e) {
                Console.Clear();
                new Thread(new ThreadStart(Utilities.sutils.BeepRepeatedly)).Start();
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
                Console.ResetColor();
                Console.ReadLine();
            }
        }

        static void mainloop(string[] args)
        {
            if (args.Length > 0)
            {
                //Some stuff
                if (args[0].Equals("-c"))
                {
                    if (args.Length == 1)
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Please provide a command after -c");
                        Console.ResetColor();
                        return;
                    } else
                    {
                        Environment.Exit(Master.interpret(String.Join(" ",args.ToList().GetRange(1, args.Length - 1))));
                    }
                }
            }
            
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
                int retcode = Master.interpret(mcommand.Replace("\n", "").Replace("\r", ""));
                
            }

        }
    }
    public static class Config {
        public static bool fullscreen = false;
        public static bool allowcolours = true;
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
                    Utilities.sutils.WriteColour("You are an administrator!", ConsoleColor.Green, true);
                } else
                {
                    Utilities.sutils.WriteColour("You are not an administrator", ConsoleColor.Red, true);
                }
            } else if (croot.Equals("crash"))
            {
                throw new SystemException("Manual Crash");
            } else if (croot.Equals("cd"))
            {
                if (largs.Length == 0)
                {
                    Console.WriteLine(Environment.CurrentDirectory);
                } else
                {
                    Environment.CurrentDirectory = largs[0];
                }
            } else if (croot.Equals("fullscreen"))
            {
                Config.fullscreen = !Config.fullscreen;//Invert boolean
                SendKeys.SendWait("{F11}");
            } else if (croot.Equals("time"))
            {
                //Linux time command
                DateTime start = DateTime.Now;
                int retcode = Master.interpret(String.Join(" ",largs).Replace("\n", "").Replace("\r", ""));
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
                        Console.WriteLine("");
                        return 1;
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.Write(":)");
                        Console.ResetColor();
                        Console.WriteLine("");
                    }
                    
                }
            } else if (croot.Equals("beep"))
            {
                int beeps = 1;
                try
                {
                    beeps = Convert.ToInt32(largs[0]);
                } catch
                {

                }
                for (int i = 0; i < beeps;i++)
                {
                    Console.Beep();
                }
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
                if (File.Exists("C:\\enderbyteprograms\\cmdp\\help.txt"))
                {
                    Console.WriteLine(File.ReadAllText("C:\\enderbyteprograms\\cmdp\\help.txt"));
                } else
                {
                    Utilities.sutils.WriteColour("Could not find help file.", ConsoleColor.Red, true);
                }
            }
            public static void Help(string[] args)
            {
                Console.WriteLine("Command Prompt Plus Help Menu\n" +
                    "\n" +
                    "Commands List:\n" +
                    "help: Show this menu\n" +
                    "exit [code]: Exit with optional exit code\n" +
                    "about: View some info about this program\n" +
                    "crash: Crash this program\n" +
                    "amiadmin: Check if user is administrator\n" +
                    "cd [dir]: Get or set the current directory\n" +
                    "time <command>: Get execution time of <command>\n" +
                    "beep [times=1]: Beep n amount of times. Default is 1");
            }
        }

    }
    namespace Utilities
    {
        public static class sutils
        {
            public static void BeepRepeatedly()
            {
                for (int i = 0; i < 5; i++)
                {
                    Console.Beep();
                }
            }
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
            public static void WriteColour(string data,ConsoleColor fgcolour,bool inclnewline)
            {
                if (Config.allowcolours)
                {
                    Console.ForegroundColor= fgcolour;
                    Console.Write(data);
                    
                    Console.ResetColor();
                } else
                {
                    Console.Write(data);
                }
                if (inclnewline)
                {
                    Console.Write("\n");
                }
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

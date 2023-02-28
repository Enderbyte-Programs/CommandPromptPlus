using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading;
using System.Web;
using Microsoft.Win32;

namespace cmdpinstall
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                EnderbyteProgramsLib.Enderlib.OptionMenu op = new EnderbyteProgramsLib.Enderlib.OptionMenu("Command Prompt Plus Installer\n(c) 2021-2023 Enderbyte Programs");
                op.AddOptions(new string[] { "Install", "Update", "Uninstall", "Repair", "Quit" });
                int dat = op.Draw();
                if (dat == 4)
                {
                    Environment.Exit(0);
                }
                else if (dat == 0)
                {
                    Console.Clear();
                    Console.WriteLine("Fetching version data...");
                    tinstall.NewInstallation();
                } else if (dat == 3)
                {
                    Console.Clear();
                    Console.WriteLine("Please wait...");
                    tinstall.RepairInstallation();
                } else if (dat == 2)
                {
                    Console.Clear();
                    Console.WriteLine("Please wait...");
                    tinstall.DoRemove();
                } else if (dat == 1)
                {
                    Console.Clear();
                    Console.WriteLine("Checking for updates");
                    tinstall.DoUpdate();
                }
            }
            catch (Exception e)
            {
                Console.Clear();
                Console.Beep();
                Console.BackgroundColor = ConsoleColor.DarkBlue;
                for (int i = 0; i < Console.WindowHeight; i++)
                {
                    Console.Write(new string(' ', Console.WindowWidth));
                }
                Console.SetCursorPosition(0, 0);
                Console.WriteLine(":(\nWe're sorry, but a fatal error occured while installing.");
                Console.WriteLine("\n" +
                    "\n" +
                    $"Type: {e.GetType().Name}\n" +
                    $"Message: {e.Message}\n" +
                    $"Stack Trace: {e.StackTrace}");
                Console.WriteLine("\n\nPlease report this full message to Enderbyte Programs");
                Console.Beep();
                Console.Write("Press enter to quit.");
                Console.ResetColor();
                Console.ReadLine();
            }

        }
    }
    public static class tinstall
    {
        private static void appShortcutToSmenu(string linkName,string linkto)
        {
            string deskDir = Environment.GetFolderPath(Environment.SpecialFolder.StartMenu);

            using (StreamWriter writer = new StreamWriter(deskDir + "\\" + linkName + ".url"))
            {
                string app = linkto;
                writer.WriteLine("[InternetShortcut]");
                writer.WriteLine("URL=file:///" + app);
                writer.WriteLine("IconIndex=0");
                string icon = app.Replace('\\', '/');
                writer.WriteLine("IconFile=" + icon);
            }
        }
        public static string dxversion = Encoding.UTF8.GetString(new WebClient().DownloadData("https://github.com/Enderbyte-Programs/CommandPromptPlus/raw/main/version.txt"));
        public static void NewInstallation()
        {
            Console.Clear();
            Console.WriteLine($"Command Prompt Plus Version {dxversion.Split(':')[0]} VID {dxversion.Split(':')[1]}");
            if (EnderbyteProgramsLib.Enderlib.util.askyesno("By Answering yes and pressing enter, you agree to install Command Prompt Plus.\n Are you sure you want to continue?"))
            {
                //Install
                Console.Clear();
                Console.WriteLine("Preparing...");
                if (Directory.Exists(Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall")))
                {
                    Directory.Delete(Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall"), true);
                }
                Directory.CreateDirectory(Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall"));
                Console.Write("Downloading: [  ] 0%   (0 KB/33 KB)\r");
                using (var client = new WebClient())
                {
                    client.DownloadFile("https://github.com/Enderbyte-Programs/CommandPromptPlus/raw/main/cmdp.exe", Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall\\cmdp.exe"));
                    Console.Write("Downloading: [# ] 50%  (30 KB/33 KB)\r");
                    client.DownloadFile("https://github.com/Enderbyte-Programs/CommandPromptPlus/raw/main/help.txt", Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall\\help.txt"));
                    Console.WriteLine("Downloading: [##] 100% (33 KB/33 KB)");
                }
                Console.WriteLine("Installing...");
                try
                { Directory.Delete("C:\\enderbyteprograms\\cmdp", true); }
                catch (Exception)
                {

                }
                string[] vdirs = new string[] { "C:\\enderbyteprograms", "C:\\enderbyteprograms\\cmdp" ,"C:\\enderbyteprograms\\cmdp\\crash_report"};
                foreach (string folder in vdirs)
                {
                    Console.WriteLine($"Installing folder {folder}");
                    if (!Directory.Exists(folder))
                    {
                        Directory.CreateDirectory(folder);
                    }
                }
                Console.WriteLine("Copying files");
                File.Copy(Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall\\cmdp.exe"), "C:\\enderbyteprograms\\cmdp\\cmdp.exe");
                File.Copy(Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall\\help.txt"), "C:\\enderbyteprograms\\cmdp\\help.txt");
                Console.WriteLine("Setting up registry");
                /*
                RegistryKey r = Registry.CurrentUser;
                RegistryKey reg = r.OpenSubKey("Environment");
                string cPATH = (string)reg.GetValue("PATH");
                if (!cPATH.Contains("C:\\enderbyteprograms\\cmdp"))
                {
                    cPATH += ";C:\\enderbyteprograms\\cmdp";
                }
                reg.SetValue("PATH", cPATH, RegistryValueKind.ExpandString);
                */
                RegistryKey epr = Registry.CurrentUser.CreateSubKey("EnderbytePrograms");
                epr = epr.CreateSubKey("cmdp");
                epr.SetValue("InstalledVersion", dxversion.Split(':')[1]);
                var name = "PATH";
                var scope = EnvironmentVariableTarget.User; // or User
                var oldValue = Environment.GetEnvironmentVariable(name, scope);
                if (!oldValue.Contains(@";C:\enderbyteprograms\cmdp"))
                { oldValue = oldValue + @";C:\enderbyteprograms\cmdp"; }
                Environment.SetEnvironmentVariable(name, oldValue, scope);
                Console.WriteLine("Creating Shortcuts");
                appShortcutToSmenu("Command Prompt Plus","C:\\enderbyteprograms\\cmdp\\cmdp.exe");
                Console.WriteLine("===========================================================================");
                Console.WriteLine("Installation complete! Run Command Prompt Plus with the cmdp command.");
                Console.WriteLine("Press any key to quit");
                Console.ReadKey();

            }
            else
            {
                Console.Clear();
                Console.WriteLine("Installation was aborted by user. Press any key to quit.");
                Console.ReadKey();
            }
        }
        public static void RepairInstallation()
        {
            string[] vdirs = new string[] { "C:\\enderbyteprograms", "C:\\enderbyteprograms\\cmdp", "C:\\enderbyteprograms\\cmdp\\crash_reports" };
            string[] vfiles = new string[] { "C:\\enderbyteprograms\\cmdp\\help.txt", "C:\\enderbyteprograms\\cmdp\\cmdp.exe" };
            string[] vdn = new string[] { "https://github.com/Enderbyte-Programs/CommandPromptPlus/raw/main/help.txt", "https://github.com/Enderbyte-Programs/CommandPromptPlus/raw/main/cmdp.exe" };
            Console.WriteLine("Verifying Directories");
            foreach (string vdir in vdirs)
            {
                Console.WriteLine($"Checking for {vdir}");
                if (Directory.Exists(vdir))
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("Yes!");
                    Console.ResetColor();
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("No. Creating");
                    Console.ResetColor();
                    Directory.CreateDirectory(vdir);
                }
            }
            int _fl = 0;
            foreach (string file in vfiles)
            {
                Console.WriteLine($"Checking for {file}");
                if (File.Exists(file))
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("Yes!");
                    Console.ResetColor();
                }
                else
                {
                    using (var client = new WebClient())
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("No. Downloading");
                        Console.ResetColor();
                        client.DownloadFile(vdn[_fl], file);
                    }
                }
                _fl++;
            }
            Console.WriteLine("Checking PATH installation");
            var name = "PATH";
            var scope = EnvironmentVariableTarget.User; // or User
            var oldValue = Environment.GetEnvironmentVariable(name, scope);
            if (!oldValue.Contains(@";C:\enderbyteprograms\cmdp"))
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Not found, fixing");
                Console.ResetColor();
                oldValue = oldValue + @";C:\enderbyteprograms\cmdp"; } else
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Yes!");
                Console.ResetColor();
            }
            Environment.SetEnvironmentVariable(name, oldValue, scope);
            Console.WriteLine("Checking Shortcuts");
            appShortcutToSmenu("Command Prompt Plus", "C:\\enderbyteprograms\\cmdp\\cmdp.exe");
            Console.WriteLine("===========================================================================");
            Console.WriteLine("Repair complete! Run Command Prompt Plus with the cmdp command.");
            Console.WriteLine("Press any key to quit");
            Console.ReadKey();

        }
        public static void DoRemove()
        {

                Console.WriteLine("Removing...");
                Directory.Delete(@"C:\enderbyteprograms\cmdp", true);
                var name = "PATH";
                var scope = EnvironmentVariableTarget.User; // or User
                var oldValue = Environment.GetEnvironmentVariable(name, scope);
                string newvalue = oldValue.Replace(@";C:\enderbyteprograms\cmdp", "");
                Environment.SetEnvironmentVariable(name,newvalue, scope);
                Registry.CurrentUser.OpenSubKey("EnderbytePrograms").DeleteSubKey("cmdp");//Delete Registry entries
                Console.WriteLine("===========================================================================");
                Console.WriteLine("Removal Complete.");
                Console.WriteLine("Press any key to quit");
                Console.ReadKey();
        }
        public static void DoUpdate()
        {

            RegistryKey iv = Registry.CurrentUser.OpenSubKey("enderbyteprograms").OpenSubKey("cmdp", true);
            if (iv == null)
            {
                Console.ForegroundColor= ConsoleColor.Red;
                Console.WriteLine("Please install command prompt plus before doing an update...");
                Console.ResetColor();
                Console.ReadKey();
                Environment.Exit(-1);
            }
            string iversion = (string)iv.GetValue("InstalledVersion");
            if (Convert.ToInt16(dxversion.Split(':')[1].Replace("\n","").Replace(" ","")) <= Convert.ToInt16(iversion))
            {
                Console.WriteLine("No new versions are available at this time\n");
                Console.WriteLine("Press any key to quit");
                Console.ReadKey();
            } else
            {
                bool installnewupdate = EnderbyteProgramsLib.Enderlib.util.askyesno($"A new version is available\n{dxversion.Split(':')[1].Replace("\n", "").Replace(" ", "")} over {iversion}");
                if (installnewupdate)
                {
                    Console.Clear();
                    Console.WriteLine("Preparing...");
                    if (Directory.Exists(Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall")))
                    {
                        Directory.Delete(Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall"), true);
                    }
                    Directory.CreateDirectory(Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall"));
                    Console.Write("Downloading: [  ] 0%   (0 KB/33 KB)\r");
                    using (var client = new WebClient())
                    {
                        client.DownloadFile("https://github.com/Enderbyte-Programs/CommandPromptPlus/raw/main/cmdp.exe", Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall\\cmdp.exe"));
                        Console.Write("Downloading: [# ] 50%  (30 KB/33 KB)\r");
                        client.DownloadFile("https://github.com/Enderbyte-Programs/CommandPromptPlus/raw/main/help.txt", Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall\\help.txt"));
                        Console.WriteLine("Downloading: [##] 100% (33 KB/33 KB)");
                    }
                    Console.WriteLine("Installing...");
                    try
                    { Directory.Delete("C:\\enderbyteprograms\\cmdp", true); }
                    catch (Exception)
                    {

                    }
                    string[] vdirs = new string[] { "C:\\enderbyteprograms", "C:\\enderbyteprograms\\cmdp" };
                    foreach (string folder in vdirs)
                    {
                        Console.WriteLine($"Installing folder {folder}");
                        if (!Directory.Exists(folder))
                        {
                            Directory.CreateDirectory(folder);
                        }
                    }
                    Console.WriteLine("Copying files");
                    File.Copy(Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall\\cmdp.exe"), "C:\\enderbyteprograms\\cmdp\\cmdp.exe");
                    File.Copy(Environment.ExpandEnvironmentVariables("%TEMP%\\cmdpinstall\\help.txt"), "C:\\enderbyteprograms\\cmdp\\help.txt");
                    Console.WriteLine("Setting up registry");
                    /*
                    RegistryKey r = Registry.CurrentUser;
                    RegistryKey reg = r.OpenSubKey("Environment");
                    string cPATH = (string)reg.GetValue("PATH");
                    if (!cPATH.Contains("C:\\enderbyteprograms\\cmdp"))
                    {
                        cPATH += ";C:\\enderbyteprograms\\cmdp";
                    }
                    reg.SetValue("PATH", cPATH, RegistryValueKind.ExpandString);
                    */
                    RegistryKey epr = Registry.CurrentUser.CreateSubKey("EnderbytePrograms");
                    epr = epr.CreateSubKey("cmdp");
                    epr.SetValue("InstalledVersion", dxversion.Split(':')[1]);
                    var name = "PATH";
                    var scope = EnvironmentVariableTarget.User; // or User
                    var oldValue = Environment.GetEnvironmentVariable(name, scope);
                    if (!oldValue.Contains(@";C:\enderbyteprograms\cmdp"))
                    { oldValue = oldValue + @";C:\enderbyteprograms\cmdp"; }
                    Environment.SetEnvironmentVariable(name, oldValue, scope);
                    appShortcutToSmenu("Command Prompt Plus", "C:\\enderbyteprograms\\cmdp\\cmdp.exe");
                    Console.WriteLine("===========================================================================");
                    Console.WriteLine("Update complete! Run Command Prompt Plus with the cmdp command.");
                    Console.WriteLine("Press any key to quit");
                    Console.ReadKey();
                }
            }
        }
    }
    namespace EnderbyteProgramsLib
    {
        namespace Enderlib
        {
            public class util
            {
                public static List<String> getfiles(String directory)
                {
                    string[] _files = Directory.GetFiles(directory);
                    return new List<String>(_files);
                }
                public static List<String> getdirs(String directory)
                {
                    string[] _files = Directory.GetDirectories(directory);
                    return new List<String>(_files);
                }
                public static String splitPathFromFile(String data)
                {
                    return data.Split('\\').ToList().Last();
                }
                public static void clearscreen()
                {
                    Console.Clear();
                }
                public static double numinput(String prompt)
                {
                    while (true)
                    {
                        String i = PyPort.std.input(prompt);
                        if (Double.TryParse(i, out double l))
                        {
                            return l;
                        }
                        else
                        {
                            Console.WriteLine("Error! Please input a number");
                        }
                    }
                }
                public static int intinput(String prompt)
                {
                    while (true)
                    {
                        String i = PyPort.std.input(prompt);
                        if (int.TryParse(i, out int l))
                        {
                            return l;
                        }
                        else
                        {
                            Console.WriteLine("Error! Please input a full integer");
                        }
                    }
                }
                public static bool askyesno(string prompt)
                {
                    while (true)
                    {
                        string i = PyPort.std.input(prompt + " (yes/no)").ToLower();
                        char c = i[0];
                        if (c == 'y' || i == "yes")
                        {
                            return true;
                        }
                        else if (c == 'n' || i == "no")
                        {
                            return false;
                        }
                        else
                        {
                            Console.WriteLine("Please input yes or no");
                        }
                    }
                }
                public static bool askyesno(string prompt, bool autocs)
                {
                    while (true)
                    {
                        string i = PyPort.std.input(prompt + " (yes/no)").ToLower();
                        char c = i[0];
                        if (c == 'y' || i == "yes")
                        {
                            return true;
                        }
                        else if (c == 'n' || i == "no")
                        {
                            return false;
                        }
                        else
                        {
                            Console.WriteLine("Please input yes or no");
                            if (autocs)
                            {
                                PyPort.time.sleep(1);
                                util.clearscreen();
                            }
                        }
                    }
                }
                public static double randd(double a, double b, int decimalplaces)
                {
                    int shift = 0;
                    while (true)
                    {
                        if (!a.ToString().Contains(".") && !b.ToString().Contains("."))
                        {
                            break;
                        }
                        else
                        {
                            a *= 10;
                            b *= 10;
                            shift++;
                        }
                    }
                    if (shift < decimalplaces)
                    {
                        a *= Math.Pow(10, decimalplaces - shift);
                        b *= Math.Pow(10, decimalplaces - shift);
                        shift = decimalplaces;
                    }
                    int _a = Convert.ToInt32(a);
                    int _b = Convert.ToInt32(b);
                    return PyPort.random.randint(_a, _b) / Math.Pow(10, shift);
                }
                public static void WaitForKP()
                {
                    Console.WriteLine("Press any key to continue");
                    Console.ReadKey();
                }
            }
            public class OptionMenu
            {
                private List<String> options = new List<String>();
                private int selected = 0;
                private string title;
                public OptionMenu(String t)
                {
                    title = t;
                }
                public void AddOption(String value)
                {
                    options.Add(value);
                }
                public void AddOptions(string[] values)
                {
                    options = options.Concat(values.ToList()).ToList();//Convert back to list
                }
                public int Draw()
                {
                    while (true)
                    {
                        util.clearscreen();
                        Console.ResetColor();
                        Console.WriteLine(title);
                        Console.WriteLine("Please choose an option with the arrow keys and enter.");
                        Console.WriteLine("===================");
                        int i;
                        for (i = 0; i < options.Count; i++)
                        {

                            if (i == selected)
                            {
                                Console.ForegroundColor = ConsoleColor.Blue;
                            }
                            Console.WriteLine(options[i]);
                            Console.ResetColor();

                        }
                        Console.WriteLine("===================");
                        ConsoleKeyInfo key = Console.ReadKey();
                        if (key.Key == ConsoleKey.DownArrow && selected < options.Count - 1)
                        {
                            selected++;
                        }
                        else if (key.Key == ConsoleKey.UpArrow && selected > 0)
                        {
                            selected--;
                        }
                        else if (key.Key == ConsoleKey.Enter)
                        {
                            util.clearscreen();
                            return selected;
                        }
                    }
                }
                public string[] GetOptions()
                {
                    return options.ToArray();
                }
            }
            public class LiveCommand
            {
                private string CommandString;
                public int exitcode;
                public string stdout;
                public string stderr;
                public LiveCommand(string commandString)
                {
                    CommandString = commandString;
                }
                public void Execute()
                {
                    //After running this, can now extract info
                    System.Diagnostics.Process process = new System.Diagnostics.Process();
                    //process.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
                    process.StartInfo.FileName = "cmd.exe";
                    process.StartInfo.Arguments = $@"/C {CommandString}";
                    process.StartInfo.UseShellExecute = false;
                    //process.StartInfo.CreateNoWindow = true;
                    //process.StartInfo.RedirectStandardOutput = true;
                    process.StartInfo.RedirectStandardError = true;
                    process.Start();

                    while (!process.HasExited)
                    {
                        //string q = process.StandardOutput.ReadToEnd();
                        string q = "";
                        string er = process.StandardError.ReadToEnd();

                        //Console.Write(q);
                        stdout += q;

                        if (er != null && er.Length > 0)
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.Write(er);
                            Console.ResetColor();//Errors in red
                            stderr += er;
                        }
                    }
                    exitcode = process.ExitCode;

                }
                public string[] GetData()
                {
                    return new string[] { exitcode.ToString(), stdout, stderr };
                }

            }

        }
        namespace PyPort
        {
            public class std
            {
                public static String input(String prompt)
                {
                    System.Console.Write(prompt + " : ");
                    String result = Console.ReadLine();

                    if (result != null)
                    {
                        return result;
                    }
                    else
                    {
                        return ""; //Returning empty if null
                    }
                }
            }
            public class str
            {

                public static String join(List<String> data, String delimeter)
                {
                    String result = "";
                    int inc = 0;
                    foreach (String s in data)
                    {
                        if (inc < data.Count() - 1)
                        {
                            result += s;
                            result += delimeter;
                            inc += 1;
                        }
                        else
                        {
                            break;
                        }
                    }
                    result += data.Last();
                    return result;
                }


                public static int count(String data, String i)
                {
                    return data.Length - data.Replace(i, "").Length;
                }
            }
            public class random
            {
                public static int randint(int a, int b)
                {
                    Random r = new Random();
                    return r.Next(a, b);
                }
                public static double rand()
                {
                    return randint(0, (int)Math.Pow(2, 63)) / Math.Pow(10, 19);
                }
                public static string choice(List<String> a)
                {
                    return a[randint(0, a.Count - 1)];
                }
            }
            public class time
            {
                public static void sleep(double seconds)
                {
                    Thread.Sleep(Convert.ToInt32(seconds * 1000));
                }
            }
        }

    }
}

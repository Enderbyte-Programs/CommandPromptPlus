using System.Runtime.InteropServices;

namespace BasicUtilities
{
    public class main
    {
        private static void interpret(String command)
        {
            if (String.Equals(command,""))
            {
                return;//Do nothing if empty
            }
            String cmd = command.Split(" ")[0];
            if (String.Equals(cmd,"exit"))
            {
                Environment.Exit(0);
                return;// ABSOLUTELY REDUNDANT BUT I DONT CARE :DDDD:D::D:D::D
            } else
            {
                Console.WriteLine("We don't know what you mean by \"{0}\"", command);
            }
        }
        private static void commandloop()
        {
            while (true)
            {
                string cwd = PythonPort.os.getcwd();
                Console.Write(cwd);
                Console.Write("> ");
                String command = PythonPort.std.input("");
                interpret(command);
            }
        }
        public static void Main(string[] args)
        {
            Boolean usefile = false;
            Boolean Astart;
            String fname = "";
            try
            {
                
                if (args.Length == 0)
                {
                    Astart = true;

                }
                else
                {
                    if (args.Contains("-c"))
                    {
                        usefile = false;
                    }
                    else
                    {
                        if (String.Equals(args[0],"--help") || String.Equals(args[0], "/?"))
                        {
                            Console.Write("Basic Utilities for .NET 6\n\nArguments:\n--help: Shows this menu\n-c: Executes command provided in addition (ex. Basic_Utilities.exe -c command -d -asd)\nA file name may also be provided in the first argument only.");
                            Environment.Exit(0);
                        }
                        usefile = true;
                        fname = args[0];
                        if (!File.Exists(fname)) {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine("Provided file does not exist!");
                            Console.ResetColor();
                            Environment.Exit(-1);
                        }
                    }
                    Astart = false;
                    usefile = false;
                }
                if (!usefile && !Astart)
                {
                    List<String> datal = new List<String>(args);
                    List<String> cdata = datal.GetRange(1, datal.Count-1);
                    interpret(PythonPort.str.join(datal, " "));
                }
                if (Astart)
                {
                    Console.WriteLine("Basic Utilities for .NET 6 version {0} (C) 2021-2022 Enderbyte Programs LLC\n", Constants.versionstring);
                    commandloop();
                } else if (usefile)
                {
                    String data = File.ReadAllText(fname);
                }
            } catch (Exception e)
            {
                Crashing.crash();
                Crashing.writecrash(e);
            }
        }
    }
    public class Constants
    {
        public static int versionid = 242;
        public static String versionstring = "3.0 beta 1";
    }
    public class Crashing//This class is thanks to some random guy on stack overflow, thank you.
    {
        [StructLayout(LayoutKind.Sequential)]
        public struct COORD
        {
            public short X;
            public short Y;
        }

        enum CharAttributes : ushort
        {
            None = 0x0000,
            FOREGROUND_BLUE = 0x0001,
            FOREGROUND_GREEN = 0x0002,
            FOREGROUND_RED = 0x0004,
            FOREGROUND_INTENSITY = 0x0008,
            BACKGROUND_BLUE = 0x0010,
            BACKGROUND_GREEN = 0x0020,
            BACKGROUND_RED = 0x0040,
            BACKGROUND_INTENSITY = 0x0080,

            COMMON_LVB_LEADING_BYTE = 0x0100,
            COMMON_LVB_TRAILING_BYTE = 0x0200,
            COMMON_LVB_GRID_HORIZONTAL = 0x0400,
            COMMON_LVB_GRID_LVERTICAL = 0x0800,
            COMMON_LVB_GRID_RVERTICAL = 0x1000,
            COMMON_LVB_REVERSE_VIDEO = 0x4000,
            COMMON_LVB_UNDERSCORE = 0x8000,
        }

        [DllImport("kernel32.dll", SetLastError = true)]
        static extern bool FillConsoleOutputAttribute(IntPtr hConsoleOutput, CharAttributes wAttribute, uint nLength, COORD dwWriteCoord, out uint lpNumberOfAttrsWritten);

        [DllImport("kernel32.dll", SetLastError = true)]
        static extern IntPtr GetStdHandle(int nStdHandle);
        public static void crash()
        {
            var stdout = GetStdHandle(-11);
            FillConsoleOutputAttribute(stdout,
                CharAttributes.BACKGROUND_BLUE | CharAttributes.FOREGROUND_BLUE | CharAttributes.FOREGROUND_RED | CharAttributes.FOREGROUND_GREEN,
                (uint)(Console.BufferWidth * Console.BufferHeight), new(), out var _);

            Console.BackgroundColor = ConsoleColor.DarkBlue;
            Console.ForegroundColor = ConsoleColor.Gray;
        }
        public static void writecrash(Exception e)
        {
            Console.Clear();
            Console.WriteLine(":(\nWe're sorry, but Basic Utilities ran in to a fatal error. Here are some details:\n");
            Console.WriteLine(PythonPort.os.getcwd());
            Console.WriteLine(Constants.versionstring);
            Console.WriteLine(e);
            Console.WriteLine("\n\n");
            PythonPort.std.input("Press enter to quit");
            Console.ResetColor();
            Environment.Exit(-1);
        }
    }
}
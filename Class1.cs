using System.Diagnostics;

namespace PythonPort
{
    /// <summary>
    /// Pythonport is a library to provide some functions common in the Python Programming language.
    /// </summary>
    public class std
    {
        //Some commands found standard with the Python interpreter
        public static String input(String prompt)
        {
            if (prompt != "")
            {
                Console.Write(prompt);
                Console.Write(" :");
            }
            String data = Console.ReadLine();
            if (data == null)
            {
                return "";//Returning nothing in unlikely event of null
            }else
            {
                return data;
            }
        }
        
    }
    public class os
    {
        /// <summary>
        /// Some common commands found in python's os library
        /// </summary>
        /// <param name="command"></param>
        /// <returns></returns>
        public static int system(String command)
        {
            Process cmd = new Process();
            cmd.StartInfo.FileName = "cmd.exe";
            cmd.StartInfo.RedirectStandardInput = true;
            cmd.StartInfo.RedirectStandardOutput = true;
            cmd.StartInfo.CreateNoWindow = false;
            cmd.StartInfo.UseShellExecute = false;
            cmd.Start();

            cmd.StandardInput.WriteLine(command);
            cmd.StandardInput.Flush();
            cmd.StandardInput.Close();
            cmd.WaitForExit();
            Console.WriteLine(cmd.StandardOutput.ReadToEnd());
            return cmd.ExitCode;
        }
        public static String getcwd()
        {
            return Directory.GetCurrentDirectory();
        }
        public static void setcwd(String data)
        {
            Directory.SetCurrentDirectory(data);
        }
    }
    public class str { 
        public static String join(List<String> data,String delimeter)
        {
            String result = "";
            int i;
            for (i = 0;i < data.Count - 2;i++)
            {
                result += data[i];
                result += delimeter;
            }
            result += data.Last();
            return result;
        }
    }
}
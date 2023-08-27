using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace csmarsu
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                string userInput = GetStrictInput();
                Console.WriteLine($"buffer: '{userInput}'");
            }
            catch (OperationCanceledException) { }
        }

        private static string GetStrictInput()
        {
            Console.WriteLine("Enter message: ");
            var builder = new StringBuilder();
            ConsoleKeyInfo keyRead = new ConsoleKeyInfo(); //< just something
            do
            {
                if (keyRead.KeyChar != '\0') //< '\r' is enter
                {
                    // input ready for sending
                    
                    if (keyRead.Key == ConsoleKey.Enter) break;

                    //bool echo = false;
                    string unused;
                    //Console.Write(keyRead.KeyChar);
                    // 1. Accept morse char, space, or enter
                    var morseCharKey = Char.ToLower(keyRead.KeyChar);
                    if (' ' == keyRead.KeyChar || _morseAlphabetDictionary.TryGetValue(morseCharKey, out unused))
                    {
                        //echo = true;
                        builder.Append(keyRead.KeyChar);
                        Console.Write(keyRead.KeyChar);
                    }
                }
                while (!Console.KeyAvailable)
                {
                    // Do something
                    //Console.Write($"key: {keyRead}");
                    Thread.Sleep(30);
                }
            } while ((keyRead = Console.ReadKey(true)).Key != ConsoleKey.Escape);
            Console.WriteLine();
            if (keyRead.Key == ConsoleKey.Escape) throw new OperationCanceledException();
            return builder.ToString();
        }

        private static IReadOnlyDictionary<char, string> _morseAlphabetDictionary = new Dictionary<char, string>
        {
            {'a', ".-"},
            {'b', "-..."},
            {'c', "-.-."},
            {'d', "-.."},
            {'e', "."},
            {'f', "..-."},
            {'g', "--."},
            {'h', "...."},
            {'i', ".."},
            {'j', ".---"},
            {'k', "-.-"},
            {'l', ".-.."},
            {'m', "--"},
            {'n', "-."},
            {'o', "---"},
            {'p', ".--."},
            {'q', "--.-"},
            {'r', ".-."},
            {'s', "..."},
            {'t', "-"},
            {'u', "..-"},
            {'v', "...-"},
            {'w', ".--"},
            {'x', "-..-"},
            {'y', "-.--"},
            {'z', "--.."},
            {'0', "-----"},
            {'1', ".----"},
            {'2', "..---"},
            {'3', "...--"},
            {'4', "....-"},
            {'5', "....."},
            {'6', "-...."},
            {'7', "--..."},
            {'8', "---.."},
            {'9', "----."}
        };

    }
}

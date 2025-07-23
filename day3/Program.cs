using System;
using System.IO;
using System.Text.RegularExpressions;

public class Program
{
    public static void Main(string[] args)
    {
        string Input = File.ReadAllText("input.txt");
        int SumOfMultsPartOne = PartOne(Input);
        int SumOfMultsPartTwo = PartTwo(Input);

        Console.WriteLine($"The total sum of valid multiplications are {SumOfMultsPartOne}.");
        Console.WriteLine($"The total sum of valid multiplications, with respect to do and don't, are {SumOfMultsPartTwo}.");
    }
    public static int PartOne(string Input)
    {
        // Regex for "mul(int1, int2)" where int1 and int2 are of length [1, 3]
        // The () around \d{1,3} creates a capturing group
        string Pattern = @"mul\((\d{1,3}),(\d{1,3})\)";

        MatchCollection ValidMults = Regex.Matches(Input, Pattern);
        int SumOfMults = 0;

        //Capturing group 0 is the whole string, 1 is int1 and 2 is int2
        foreach (Match match in ValidMults)
        {
            int int1 = int.Parse(match.Groups[1].Value);
            int int2 = int.Parse(match.Groups[2].Value);
            SumOfMults += int1 * int2;
        }
        return SumOfMults;
    }

    public static int PartTwo(string Input)
    {
        //Regex for all matches of previous mul, but also for "do()" and "don't()"
        string Pattern = @"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)";

        MatchCollection ValidMults = Regex.Matches(Input, Pattern);
        int SumOfMults = 0;
        bool MultEnabled = true;

        foreach (Match match in ValidMults)
        {
            if (match.Value == "do()")
            {
                MultEnabled = true;
            }
            else if (match.Value == "don't()")
            {
                MultEnabled = false;
            }
            else if (MultEnabled)
            {
                int int1 = int.Parse(match.Groups[1].Value);
                int int2 = int.Parse(match.Groups[2].Value);
                SumOfMults += int1 * int2;
            }
        }
        return SumOfMults;
    }
}
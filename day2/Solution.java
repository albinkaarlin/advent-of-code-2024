
package day2;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {
    public static void main(String[] args) {

        try {
            List<String> reportList = parsing();
            int safeReportsPartOne = countSafeReports(reportList, 1);
            int safeReportsPartTwo = countSafeReports(reportList, 2);

            System.out.println("The total amount of safe reports are " + safeReportsPartOne + ".");
            System.out.println("The total amount of safe reports with Problem Dampener are " + safeReportsPartTwo + ".");

        } 
        catch (IOException e) {
            e.printStackTrace();
        }
    }

//----------------------------------------------------------------------------------------------------------------------------------

    public static List<String> parsing() throws IOException{

        List<String> inputList = Files.readAllLines(Paths.get("day2/input.txt"));
        return inputList;
    }

//----------------------------------------------------------------------------------------------------------------------------------

    public static int countSafeReports(List<String> reportList, int part) {

        int safeReports = 0;
        for (String line : reportList) {
            List<Integer> report = Arrays.stream(line.trim().split("\\s+"))
                              .map(Integer::parseInt)
                              .collect(Collectors.toList());
            switch (part) {
                case 1:
                    if (checkReport(report)) {
                        safeReports++;
                    }
                    break;
            
                case 2:
                    if (checkReportWithProbDamp(report)) {
                        safeReports++;
                    }
                    break;
            }
        }
        return safeReports;
    }

    //----------------------------------------------------------------------------------------------------------------------------------

    private static boolean checkReport(List<Integer> report) {
        int length = report.size();

        if (length < 2) {
            return true;
        }

        boolean increasing = report.get(0) < report.get(1);
        boolean decreasing = report.get(0) > report.get(1);

        for (int i = 0; i < length-1; i++) {
            int diff = report.get(i) - report.get(i+1);
            int absDiff = Math.abs(diff);

            if (absDiff < 1 || absDiff > 3) {
                return false;
            }
            else if (increasing && diff > 0) {
                return false;
            }
            else if (decreasing && diff < 0) {
                return false;
            }
        }

        return increasing || decreasing;
    }

    //----------------------------------------------------------------------------------------------------------------------------------

    private static boolean checkReportWithProbDamp(List<Integer> report) {
        if (checkReport(report)) {
            return true;
        }

        int length = report.size();

        for (int i = 0; i < length; i++) {
            List<Integer> reducedReport = new ArrayList<>(length - 1);

            for (int j = 0; j < length; j++) {
                if (i != j) {
                    reducedReport.add(report.get(j));
                }
            }

            if (checkReport(reducedReport)) {
                return true;
            }
        }
        return false;
    }

}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class fileManage {
    public static String readFileContent(String filename) {

        byte[] fileContent;
        String binary = "";
        try {
            fileContent = Files.readAllBytes(new File(filename).toPath());
            binary = toBinary(fileContent);
        }

        catch (IOException e) {
            System.err.println("File not found");
        } catch (NullPointerException e) {
            System.err.println("incomplete read file");
        }

        return binary;
    }

    public static String readByteInfile(String filePath) {
        String line;
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            while ((line = reader.readLine()) != null) {
                // Process each line (string)
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return "";
    }

    // read file and convert to binary
    public static String toBinary(byte[] bytes) {
        StringBuilder sb = new StringBuilder(bytes.length * Byte.SIZE);
        for (long i = 0; i < Byte.SIZE * bytes.length; i++)
            sb.append((bytes[(int) i / Byte.SIZE] << i % Byte.SIZE & 0x80) == 0 ? '0' : '1');
        return sb.toString();
    }

    public static void writeFile(String fileName, int[][] intArray) {
        if (fileName == null || fileName.isEmpty()) {
            System.out.println("File name is empty or null.");
            return;
        }

        try (FileOutputStream fos = new FileOutputStream(fileName);
                DataOutputStream dos = new DataOutputStream(fos)) {

            // Write each integer as a byte
            for (int[] row : intArray) {
                for (int num : row) {
                    byte byt = (byte) (num);
                    String s = Integer.toHexString(byt & 0xff);
                    System.out.println("write \\x" + s);
                    dos.writeChars("\\x" + s);
                }
                dos.writeChars("\n");
            }

            System.out.println("Array written to file successfully.");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

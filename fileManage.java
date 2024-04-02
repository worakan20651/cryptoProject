import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
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
    // read file and convert to binary
    public static String toBinary(byte[] bytes) {
        StringBuilder sb = new StringBuilder(bytes.length * Byte.SIZE);
        for (long i = 0; i < Byte.SIZE * bytes.length; i++)
            sb.append((bytes[(int) i / Byte.SIZE] << i % Byte.SIZE & 0x80) == 0 ? '0' : '1');
        return sb.toString();
    }

    public static void writeFile(String fileName, String content) {
        if (fileName == null || fileName.isEmpty()) {
            System.out.println("File name is empty or null.");
            return;
        }
        try {
            // Create a FileOutputStream object
            FileOutputStream fos = new FileOutputStream(fileName);
    
            // Convert the string to bytes and write to the file
            fos.write(content.getBytes());
    
            // Close the stream
            fos.close();
    
            System.out.println("Content written to file successfully.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}

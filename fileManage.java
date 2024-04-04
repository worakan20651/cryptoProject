import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.ByteBuffer;


public class fileManage {
    public  static String readFileContent(String filename) {

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

    public static byte[] readByteInfile(String filename) {
        byte[] fileContent;
        try {
            fileContent = Files.readAllBytes(new File(filename).toPath());
            System.out.println("test read byte "+ByteBuffer.wrap(fileContent).getInt());
            return fileContent;

        } catch (IOException e) {
            e.printStackTrace();
        }
        return new byte[0];
    }

    // read file and convert to binary
    public static String toBinary(byte[] bytes) {
        StringBuilder sb = new StringBuilder(bytes.length * Byte.SIZE);
        for (long i = 0; i < Byte.SIZE * bytes.length; i++)
            sb.append((bytes[(int) i / Byte.SIZE] << i % Byte.SIZE & 0x80) == 0 ? '0' : '1');
        return sb.toString();
    }

    
    public static String writeBinary(String content, String fileName) {
        String tmpFile = "tmp_"+fileName;
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(tmpFile));
            writer.write(content);
            writer.close();
            // System.out.printf("File %s has been written successfully.\n",tmpFile);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }

        return tmpFile;
    }
}

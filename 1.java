import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入第一个数字：");
        int a = scanner.nextInt();
        System.out.print("请输入第二个数字：");
        int b = scanner.nextInt();
        if (a % b == 0) {
            System.out.println("结果是：" + (a + b));
        } else {
            System.out.println("结果是：" + (a - b));
        }
        scanner.close();
    }
}
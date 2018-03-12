package a.b;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.text.SimpleDateFormat;
import java.util.Arrays;

/**
 * Hello world!
 */
public class App {

    private static final Logger LOGGER= LoggerFactory.getLogger(App.class);

    public static void main(String[] args) {
        LOGGER.info("begin : "+new SimpleDateFormat("yyyy-MM-dd HH:mm:ss,SSS"));
        System.out.println("Hello World!");
        Arrays.asList(args).stream().forEach(str->LOGGER.info(str+"\n"));
        LOGGER.info("end : "+new SimpleDateFormat("yyyy-MM-dd HH:mm:ss,SSS"));
    }
}

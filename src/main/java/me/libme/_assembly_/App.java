package me.libme._assembly_;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.concurrent.TimeUnit;

/**
 * Hello world!
 */
public class App {

    private static final Logger LOGGER= LoggerFactory.getLogger(App.class);

    public static void main(String[] args) throws InterruptedException {
        LOGGER.info("begin : "+new SimpleDateFormat("yyyy-MM-dd HH:mm:ss,SSS").format(new Date()));
        System.out.println("======================Hello World!==========================");
        Arrays.asList(args).stream().forEach(str->LOGGER.info(str+"\n"));
        LOGGER.info("end : "+new SimpleDateFormat("yyyy-MM-dd HH:mm:ss,SSS").format(new Date()));

        TimeUnit.SECONDS.sleep(10);
        System.out.println("====================== End !==========================");
    }
}

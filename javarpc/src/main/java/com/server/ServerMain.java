package com.server;

import org.apache.thrift.TMultiplexedProcessor;
import org.apache.thrift.TProcessor;
import org.apache.thrift.TProcessorFactory;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TThreadedSelectorServer;
import org.apache.thrift.transport.TFramedTransport;
import org.apache.thrift.transport.TNonblockingServerSocket;
import org.apache.thrift.transport.TNonblockingServerTransport;

import java.net.InetSocketAddress;

/**
 * @author: ljyang
 * @date: 2019/11/4 11:37
 * @description
 */

public class ServerMain {
    public static void main(String[] args) throws Exception{
        // 创建一个transport，server端响应模式
        TNonblockingServerTransport tServerTransport = new TNonblockingServerSocket(new InetSocketAddress("127.0.0.1", 9999));

        // 构建server端的参数
        TThreadedSelectorServer.Args tArgs = new TThreadedSelectorServer.Args(tServerTransport);

        //创建一个processor(handler事件处理器)
        TProcessor tProcessor = new Calculator.Processor<>(new CalculatorImpl());
        //创建多重事件处理器
        TMultiplexedProcessor multiplexedProcessor = new TMultiplexedProcessor();
        //添加事件处理器
        multiplexedProcessor.registerProcessor("calService", tProcessor);

        //添加多重事件处理器
        tArgs.processorFactory(new TProcessorFactory(multiplexedProcessor));

        //添加序列化格式
        tArgs.protocolFactory(new TBinaryProtocol.Factory());

        //添加消息传输模式
        tArgs.transportFactory(new TFramedTransport.Factory());

        //selector的线程数（selector线程负责读写IO）
        tArgs.selectorThreads(2);
        // 每个selector线程的任务队列大小
        tArgs.acceptQueueSizePerThread(4);
        // 执行任务的线程数
        tArgs.workerThreads(3);
        // 执行任务的线程池，默认会创建一个FixeThreadPoolExecutor
        // tArgs.executorService();

        tArgs.acceptPolicy(TThreadedSelectorServer.Args.AcceptPolicy.FAIR_ACCEPT);

        //根据args创建一个指定类型的server
        TServer tServer = new TThreadedSelectorServer(tArgs);
        tServer.serve();
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            tServer.stop();
        }));
    }
}

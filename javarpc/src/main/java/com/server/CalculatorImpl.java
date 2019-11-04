package com.server;

import org.apache.thrift.TException;
import com.server.calserver.Calculate;
import com.server.calserver.CalculateFactory;

/**
 * @author: ljyang
 * @date: 2019/11/4 13:46
 * @description
 */

public class CalculatorImpl implements Calculator.Iface {
    @Override
    public int getResult(CalParam param) throws calException, TException {
        if(param == null){
            throw new calException();
        }
        int res = 0;
        int num1 = param.num1;
        int num2 = param.num2;
        Operation op = param.op;

        CalculateFactory calculateFactory = new CalculateFactory();
        Calculate calculate = calculateFactory.getCalculate(op);

        return calculate.operate(num1, num2);
    }

}

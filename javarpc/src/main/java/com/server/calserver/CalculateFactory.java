package com.server.calserver;

import com.server.Operation;

/**
 * @author: ljyang
 * @date: 2019/11/4 13:59
 * @description
 */

public class CalculateFactory {
    public Calculate getCalculate(Operation op){
        Calculate calculate = null;
        switch (op){
            case ADD:
                calculate = new AddCalculate();
                break;
            case MULTIPLY:
                calculate = new MulCalculate();
                break;
            case DIVIDE:
                calculate = new DivCalculate();
                break;
            case SUBTRACT:
                calculate = new SubCalculate();
                break;
            default:
                break;
        }
        return calculate;
    }

    static class AddCalculate implements Calculate{

        @Override
        public int operate(int num1, int num2) {
            return num1 + num2;
        }
    }

    static class SubCalculate implements Calculate{

        @Override
        public int operate(int num1, int num2) {
            return num1 - num2;
        }
    }

    static class MulCalculate implements Calculate{
        @Override
        public int operate(int num1, int num2) {
            return num1 * num2;
        }
    }

    static class DivCalculate implements Calculate{

        @Override
        public int operate(int num1, int num2) {
            return num1 / num2;
        }
    }
}

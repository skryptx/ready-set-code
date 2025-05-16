package Inheritence.MultipleInheritence;

import Inheritence.MultipleInheritence.Enums.DeviceState;
import Inheritence.MultipleInheritence.Interfaces.Device;
import Inheritence.MultipleInheritence.Interfaces.Machine;

public class DeviceRunner {
    public static void main(String[] args) {
        Device mobile = new Mobile();
        Machine mobileV2 = (Machine)mobile;

        mobile.changeState(DeviceState.ON);
        System.out.println(((Mobile)mobile).getState());
        mobile.turnOnCamera();

        mobileV2.changeState(DeviceState.OFF);
        System.out.println(((Mobile)mobile).getState());
    }
}

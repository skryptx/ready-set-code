package Inheritence.MultipleInheritence;

import Inheritence.MultipleInheritence.Enums.DeviceState;
import Inheritence.MultipleInheritence.Interfaces.Device;
import Inheritence.MultipleInheritence.Interfaces.Machine;

public class Mobile implements Device, Machine {
    DeviceState state = DeviceState.OFF;

    public DeviceState getState() {
        return state;
    }

    public void changeState(DeviceState state) {
        this.state = state;
    }

    public void turnOnCamera() {
        System.out.println("Turned On Camera");
    }
}

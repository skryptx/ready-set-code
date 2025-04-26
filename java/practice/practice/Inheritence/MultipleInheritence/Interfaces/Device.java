package Inheritence.MultipleInheritence.Interfaces;

import Inheritence.MultipleInheritence.Enums.DeviceState;

public interface Device {
    default void changeState(DeviceState state) {
        System.out.println("Calling Interface default method. Nothing Happens.");
    }

    void turnOnCamera();
}

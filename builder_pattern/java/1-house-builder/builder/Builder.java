package builder;


public interface Builder {

    void setBuildingType(BuildingType type);

    void setNumberWalls(int numberWalls);

    void setNumberWindows(int numberWindows);

    void setWindowType(WindowType type);

    void setNumberDoors(int numberDoors);

    void setDoorType(DoorType type);
}

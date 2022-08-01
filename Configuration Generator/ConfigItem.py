# importing enum for enumerations
import enum
 
# creating enumerations using class
class PrimitiveTypes(enum.Enum):
    string = 1
    boolean = 2
    uint8 = 3
    uint16 = 4
    uint32 = 5
    uint64 = 6
    int8 = 7
    int16 = 8
    int32 = 9
    int64 = 10
    double = 11
    datetime = 12
    email = 13
    
class ConfigItem:
    def __init__(self, a_type, a_configTitle, default, lowerRange, upperRange):
        self.m_type = a_type;
        self.m_configTitle = a_configTitle;
        self.m_currValue = default;
        self.m_lowerRange = lowerRange;
        self.m_upperRange = upperRange;
        
        
    
    def validate(self):
        if (self.m_type == PrimitiveTypes.string):
            if (len(self.m_currValue) < self.m_lowerRange):
                self.m_currValue = self.m_currValue.ljust(self.m_lowerRange- len(self.m_currValue), '0') ;
                return False;
            if (len(self.m_currValue) > self.m_upperRange):
                self.m_currValue = self.m_currValue[0|self.m_upperRange];
        if  (self.m_type == PrimitiveTypes.double or 
             self.m_type == PrimitiveTypes.int8 or 
             self.m_type == PrimitiveTypes.int16 or 
             self.m_type == PrimitiveTypes.int32 or
             self.m_type == PrimitiveTypes.int64 or
             self.m_type == PrimitiveTypes.uint8 or 
             self.m_type == PrimitiveTypes.uint16 or 
             self.m_type == PrimitiveTypes.uint32 or
             self.m_type == PrimitiveTypes.uint64 or
             self.m_type == PrimitiveTypes.datetime):
            if (self.m_currValue < self.m_lowerRange):
                self.m_currValue = self.m_lowerRange;
            if (self.m_currValue > self.m_upperRange): 
                self.m_currValue = self.m_upperRange;
            return False;
        if (self.m_type == PrimitiveTypes.email):
            if (self.m_currValue.__contains__("@")):
                return True;
            else:
                return False;
        return True;
            
    
#!/usr/bin/env python3
"""
JMRI Configuration Generator for COVA Layout

Generates JMRI XML configuration sections from a master data source.
Reads master data (JSON) and outputs valid JMRI XML that can be merged
into an existing layout configuration.

Usage:
    python3 jmri_config_gen.py --input cova_layout_master_data.json --output generated_config.xml
"""

import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime
import argparse


@dataclass
class TurnoutConfig:
    """Represents a single turnout configuration"""
    id: str
    user_name: str
    address: str
    control_system: str  # MQTT, SPROG, LCC
    feedback: str = "DIRECT"
    inverted: bool = False
    
    def to_mqtt_xml(self) -> ET.Element:
        """Generate MQTT turnout XML element"""
        elem = ET.Element("turnout")
        elem.set("feedback", self.feedback)
        elem.set("inverted", str(self.inverted).lower())
        elem.set("automate", "Off")
        
        sys_name = ET.SubElement(elem, "systemName")
        sys_name.text = self.address
        
        user_name = ET.SubElement(elem, "userName")
        user_name.text = self.user_name
        
        return elem
    
    def to_sprog_xml(self) -> ET.Element:
        """Generate SPROG turnout XML element"""
        elem = ET.Element("turnout")
        elem.set("feedback", self.feedback)
        elem.set("inverted", str(self.inverted).lower())
        elem.set("automate", "Off")
        
        sys_name = ET.SubElement(elem, "systemName")
        sys_name.text = self.address
        
        user_name = ET.SubElement(elem, "userName")
        user_name.text = self.user_name
        
        return elem


@dataclass
class SensorConfig:
    """Represents a single sensor configuration"""
    id: str
    user_name: str
    lcc_event_id: str
    control_system: str = "LCC"
    
    def to_lcc_xml(self) -> ET.Element:
        """Generate LCC/OpenLCB sensor XML element"""
        elem = ET.Element("sensor")
        elem.set("inverted", "false")
        
        sys_name = ET.SubElement(elem, "systemName")
        sys_name.text = self.lcc_event_id
        
        user_name = ET.SubElement(elem, "userName")
        user_name.text = self.user_name
        
        return elem


class JMRIConfigGenerator:
    """Main generator class"""
    
    def __init__(self, master_data_path: str):
        """
        Initialize generator with master data
        
        Args:
            master_data_path: Path to JSON master data file
        """
        self.master_data_path = Path(master_data_path)
        self.data = self._load_master_data()
        self.mqtt_turnouts: List[TurnoutConfig] = []
        self.sprog_turnouts: List[TurnoutConfig] = []
        self.lcc_sensors: List[SensorConfig] = []
        self._parse_master_data()
    
    def _load_master_data(self) -> Dict[str, Any]:
        """Load and parse JSON master data"""
        with open(self.master_data_path, 'r') as f:
            return json.load(f)
    
    def _parse_master_data(self):
        """Parse master data and organize into typed configurations"""
        for area_name, area_data in self.data.get("areas", {}).items():
            # Parse turnouts
            for turnout in area_data.get("turnouts", []):
                config = TurnoutConfig(
                    id=turnout["id"],
                    user_name=turnout["user_name"],
                    address=turnout["address"],
                    control_system=turnout["control_system"],
                    feedback=turnout.get("feedback", "DIRECT"),
                    inverted=turnout.get("inverted", False)
                )
                
                if turnout["control_system"] == "MQTT":
                    self.mqtt_turnouts.append(config)
                elif turnout["control_system"] == "SPROG":
                    self.sprog_turnouts.append(config)
            
            # Parse sensors
            for sensor in area_data.get("occupancy_sensors", []):
                config = SensorConfig(
                    id=sensor["id"],
                    user_name=sensor["user_name"],
                    lcc_event_id=sensor["lcc_event_id"],
                    control_system="LCC"
                )
                self.lcc_sensors.append(config)
    
    def generate_mqtt_turnouts_section(self) -> ET.Element:
        """Generate <turnouts class="jmri.jmrix.mqtt..."> XML section"""
        root = ET.Element("turnouts")
        root.set("class", "jmri.jmrix.mqtt.configurexml.MqttTurnoutManagerXml")
        
        # Add operations configuration
        operations = ET.SubElement(root, "operations")
        operations.set("automate", "false")
        
        for op_name, op_class in [
            ("NoFeedback", "jmri.configurexml.turnoutoperations.NoFeedbackTurnoutOperationXml"),
            ("Raw", "jmri.configurexml.turnoutoperations.RawTurnoutOperationXml"),
            ("Sensor", "jmri.configurexml.turnoutoperations.SensorTurnoutOperationXml")
        ]:
            op = ET.SubElement(operations, "operation")
            op.set("name", op_name)
            op.set("class", op_class)
            op.set("interval", "300")
            op.set("maxtries", "2" if op_name == "NoFeedback" else "1" if op_name == "Raw" else "3")
        
        # Add speed defaults
        ET.SubElement(root, "defaultclosedspeed").text = "Normal"
        ET.SubElement(root, "defaultthrownspeed").text = "Restricted"
        
        # Add turnout definitions
        for turnout in self.mqtt_turnouts:
            root.append(turnout.to_mqtt_xml())
        
        return root
    
    def generate_sprog_turnouts_section(self) -> ET.Element:
        """Generate <turnouts class="jmri.jmrix.sprog..."> XML section"""
        root = ET.Element("turnouts")
        root.set("class", "jmri.jmrix.sprog.configurexml.SprogTurnoutManagerXml")
        
        # Add operations configuration (same as MQTT)
        operations = ET.SubElement(root, "operations")
        operations.set("automate", "false")
        
        for op_name, op_class in [
            ("NoFeedback", "jmri.configurexml.turnoutoperations.NoFeedbackTurnoutOperationXml"),
            ("Raw", "jmri.configurexml.turnoutoperations.RawTurnoutOperationXml"),
            ("Sensor", "jmri.configurexml.turnoutoperations.SensorTurnoutOperationXml")
        ]:
            op = ET.SubElement(operations, "operation")
            op.set("name", op_name)
            op.set("class", op_class)
            op.set("interval", "300")
            op.set("maxtries", "2" if op_name == "NoFeedback" else "1" if op_name == "Raw" else "3")
        
        # Add speed defaults
        ET.SubElement(root, "defaultclosedspeed").text = "Normal"
        ET.SubElement(root, "defaultthrownspeed").text = "Restricted"
        
        # Add turnout definitions
        for turnout in self.sprog_turnouts:
            root.append(turnout.to_sprog_xml())
        
        return root
    
    def generate_lcc_sensors_section(self) -> ET.Element:
        """Generate <sensors class="jmri.jmrix.openlcb..."> XML section"""
        root = ET.Element("sensors")
        root.set("class", "jmri.jmrix.openlcb.configurexml.OlcbSensorManagerXml")
        
        for sensor in self.lcc_sensors:
            root.append(sensor.to_lcc_xml())
        
        return root
    
    def generate_config(self) -> str:
        """
        Generate complete JMRI configuration XML
        
        Returns:
            Pretty-printed XML string
        """
        root = ET.Element("jmri_generated_config")
        root.set("generated", datetime.now().isoformat())
        root.set("layout_name", self.data.get("metadata", {}).get("layout_name", "COVA"))
        
        # Add sections
        if self.lcc_sensors:
            root.append(self.generate_lcc_sensors_section())
        if self.mqtt_turnouts:
            root.append(self.generate_mqtt_turnouts_section())
        if self.sprog_turnouts:
            root.append(self.generate_sprog_turnouts_section())
        
        # Pretty-print
        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
        
        return xml_str
    
    def generate_and_write(self, output_path: str):
        """Generate config and write to file"""
        xml_content = self.generate_config()
        
        with open(output_path, 'w') as f:
            f.write(xml_content)
        
        print(f"Generated JMRI config: {output_path}")
        print(f"  - {len(self.lcc_sensors)} LCC sensors")
        print(f"  - {len(self.mqtt_turnouts)} MQTT turnouts")
        print(f"  - {len(self.sprog_turnouts)} SPROG turnouts")


def main():
    parser = argparse.ArgumentParser(
        description="Generate JMRI XML configuration from master data"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to master data JSON file"
    )
    parser.add_argument(
        "--output",
        default="generated_jmri_config.xml",
        help="Output XML file path (default: generated_jmri_config.xml)"
    )
    
    args = parser.parse_args()
    
    try:
        gen = JMRIConfigGenerator(args.input)
        gen.generate_and_write(args.output)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        exit(1)


if __name__ == "__main__":
    main()

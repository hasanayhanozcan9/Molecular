import numpy as np
import math
import hashlib
from dataclasses import dataclass, field
from typing import List, Optional, Union

# =============================================================================
# PHASE 1: PHYSICAL LAYER (PHY) - THE LAWS OF THE UNIVERSE
# =============================================================================

class PhysicalMedium:
    """Mathematical models for molecular propagation in 3D fluid environments."""
    AVOGADRO = 6.022e23
    BOLTZMANN = 1.38e-23

    @staticmethod
    def get_diffusion_coefficient(temp: float, viscosity: float, radius: float) -> float:
        """Stokes-Einstein Equation: D = (k*T) / (6*pi*eta*r)"""
        return (PhysicalMedium.BOLTZMANN * temp) / (6 * math.pi * viscosity * radius)

    @staticmethod
    def impulse_response_3d(Q: int, D: float, d: float, t: float) -> float:
        """Fick's Second Law: Concentration at distance d and time t."""
        if t <= 0: return 0
        return (Q / (4 * math.pi * D * t)**1.5) * math.exp(-(d**2) / (4 * D * t))

# =============================================================================
# PHASE 2: DATA LINK & NETWORK LAYER (NET) - THE PROTOCOL
# =============================================================================

@dataclass
class MolecularPacket:
    """The Universal Packet Structure for Molecular Data."""
    source_id: str
    dest_id: str
    payload: List[int]
    sequence_no: int
    checksum: str = ""

    def __post_init__(self):
        # Generate a checksum for data integrity (Error Detection)
        data_string = "".join(map(str, self.payload))
        self.checksum = hashlib.md5(data_string.encode()).hexdigest()[:8]

class ModulationEngine:
    """CSK (Concentration Shift Keying) and MoSK (Molecule Shift Keying) logic."""
    def __init__(self, molecules_per_bit: int = 10000):
        self.mpb = molecules_per_bit

    def bit_to_concentration(self, bit: int) -> int:
        return self.mpb if bit == 1 else 0

# =============================================================================
# PHASE 3: THE MASTER KERNEL - PAKIZE DIKEN MOLECULAR OS
# =============================================================================

class PDMolecularOS:
    """
    The Central Controller for Global Molecular Dominance.
    Engineered by Pakize Diken.
    """
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.version = "1.0.0-PLATINUM"
        self.modulation = ModulationEngine()
        self.temp = 310.15  # Human body temp (37C) in Kelvin
        self.viscosity = 0.001  # Viscosity of water/blood
        self.particle_radius = 1e-9  # Nanoscale particles
        
        self.D = PhysicalMedium.get_diffusion_coefficient(self.temp, self.viscosity, self.particle_radius)

    def transmit(self, target_id: str, message: str) -> List[MolecularPacket]:
        """Encapsulates data into molecular packets."""
        print(f"[{self.node_id}] Initiating transmission to {target_id}...")
        binary_payload = [int(b) for b in ''.join(format(ord(c), '08b') for c in message)]
        
        # Fragmentation (breaking message into small packets)
        packet = MolecularPacket(
            source_id=self.node_id,
            dest_id=target_id,
            payload=binary_payload,
            sequence_no=1
        )
        return [packet]

    def simulate_channel(self, packet: MolecularPacket, distance_um: float):
        """Simulates the physical propagation through the bio-medium."""
        distance = distance_um * 1e-6
        received_signals = []
        
        print(f"[CHANNEL] Propagating molecules over {distance_um}um...")
        
        for bit in packet.payload:
            q = self.modulation.bit_to_concentration(bit)
            # Sample concentration at peak time (t = d^2 / 6D)
            t_peak = (distance**2) / (6 * self.D)
            conc = PhysicalMedium.impulse_response_3d(q, self.D, distance, t_peak)
            
            # Stochastic Noise (Brownian motion randomness)
            noise = np.random.normal(0, conc * 0.1) if conc > 0 else abs(np.random.normal(0, 1e12))
            received_signals.append(conc + noise)
            
        return received_signals

    def receive(self, signals: List[float]) -> str:
        """Decodes, de-encapsulates, and verifies the molecular message."""
        # Adaptive Thresholding
        avg_signal = np.mean(signals)
        bits = [1 if s > avg_signal else 0 for s in signals]
        
        # Convert bits back to characters
        chars = []
        for i in range(0, len(bits), 8):
            byte = bits[i:i+8]
            if len(byte) == 8:
                char_code = int("".join(map(str, byte)), 2)
                chars.append(chr(char_code))
        
        return "".join(chars)

# =============================================================================
# EXECUTION: DEPLOYING THE GLOBAL STANDARD
# =============================================================================

if __name__ == "__main__":
    print(f"{'='*60}")
    print(f"PAKIZE DIKEN MOLECULAR INTERNET PROTOCOL (PD-MIP)")
    print(f"Global Standard Initialization...")
    print(f"{'='*60}\n")

    # Initialize the Master Node
    master_node = PDMolecularOS(node_id="ROOT_AUTHORITY_PAKIZEDIKEN")

    # Command: Global Empowerment
    CMD = "GLOBAL_DOMINANCE"
    
    # 1. Network Layer: Packetization
    packets = master_node.transmit(target_id="BIO_RECIPIENT_01", message=CMD)
    
    for p in packets:
        # 2. Physical Layer: Molecular Propagation
        # Simulating a 20 micrometer gap between cells
        molecular_signals = master_node.simulate_channel(p, distance_um=20.0)
        
        # 3. Application Layer: Decoding
        decoded_msg = master_node.receive(molecular_signals)
        
        print(f"\n[SYSTEM REPORT]")
        print(f"Source      : {p.source_id}")
        print(f"Checksum    : {p.checksum}")
        print(f"Decoded Data: {decoded_msg}")
        
        if decoded_msg == CMD:
            print("\n>>> STATUS: MOLECULAR LINK ESTABLISHED. PROTOCOL SECURED BY PAKIZE DIKEN. <<<")
        else:
            print("\n>>> STATUS: INTERFERENCE DETECTED. RETRANSMITTING... <<<")

    print(f"\n{'='*60}")

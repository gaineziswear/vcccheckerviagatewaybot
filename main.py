#!/usr/bin/env python3
"""
VCC Checker via Gateway Bot - Main Entry Point
Bank-level credit card validation testing system
"""

import asyncio
import logging
import sys
import os

# Add src to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.core.quantum_generator import QuantumCardGenerator
from src.gateways.gateway_orchestrator import MultiGatewayOrchestrator
from src.security.bank_monitor import SecurityMonitor

async def main():
    """Main execution function"""
    print("🚀 VCC Checker Gateway Bot Starting...")
    
    try:
        # Initialize components
        generator = QuantumCardGenerator()
        orchestrator = MultiGatewayOrchestrator()
        security_monitor = SecurityMonitor()
        
        print("✅ Components initialized")
        
        # Generate test cards
        test_cards = await generator.generate_batch(10)
        print(f"✅ Generated {len(test_cards)} test cards")
        
        # Test through gateways
        results = await orchestrator.coordinated_test(test_cards, security_monitor)
        print(f"✅ Completed testing through {len(results)} gateways")
        
        print("🎉 VCC Checker execution completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())

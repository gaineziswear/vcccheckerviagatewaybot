# src/gateways/gateway_orchestrator.py
import asyncio
import aiohttp
from typing import List, Dict
from .nexus_checker import NexusChecker
from .stripe_gateway import StripeGateway
from .paypal_gateway import PayPalGateway
import logging

class MultiGatewayOrchestrator:
    """Orchestrate testing across multiple payment gateways"""
    
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.gateways = self._initialize_gateways()
        
    def _initialize_gateways(self) -> Dict:
        """Initialize all gateway connectors"""
        return {
            'nexus': NexusChecker(self.config),
            'stripe': StripeGateway(self.config),
            'paypal': PayPalGateway(self.config),
            'braintree': BraintreeGateway(self.config),
            'authorize_net': AuthorizeNetGateway(self.config),
            'square': SquareGateway(self.config),
            'adyen': AdyenGateway(self.config),
        }
    
    async def coordinated_test(self, cards: List[str], security_monitor) -> Dict:
        """Run coordinated testing across all gateways"""
        results = {}
        
        for gateway_name, gateway in self.gateways.items():
            self.logger.info(f"Testing through {gateway_name} gateway...")
            
            # Apply rate limiting
            await security_monitor.check_rate_limit(gateway_name)
            
            # Test cards through gateway
            gateway_results = await self._test_gateway_batch(gateway, cards[:10])
            results[gateway_name] = gateway_results
            
            # Security monitoring
            await security_monitor.record_gateway_activity(gateway_name, gateway_results)
            
        return results
    
    async def _test_gateway_batch(self, gateway, cards: List[str]) -> List[Dict]:
        """Test batch of cards through a single gateway"""
        tasks = []
        for card in cards:
            task = gateway.validate_card(card)
            tasks.append(task)
        
        return await asyncio.gather(*tasks, return_exceptions=True)
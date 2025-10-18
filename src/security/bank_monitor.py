# src/security/bank_monitor.py
import asyncio
import time
from typing import List, Dict
import logging

class SecurityMonitor:
    """Monitor testing activities for security compliance"""
    
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.activity_log = []
        self.rate_limits = {}
        
    async def check_rate_limit(self, gateway: str) -> bool:
        """Check and enforce rate limits"""
        current_time = time.time()
        gateway_key = f"rate_limit_{gateway}"
        
        if gateway_key not in self.rate_limits:
            self.rate_limits[gateway_key] = []
        
        # Clean old entries (last minute)
        self.rate_limits[gateway_key] = [
            t for t in self.rate_limits[gateway_key] 
            if current_time - t < 60
        ]
        
        max_requests = self.config.get(f'gateways.{gateway}.max_requests_per_minute', 10)
        
        if len(self.rate_limits[gateway_key]) >= max_requests:
            await asyncio.sleep(60 - (current_time - self.rate_limits[gateway_key][0]))
            return await self.check_rate_limit(gateway)
        
        self.rate_limits[gateway_key].append(current_time)
        return True
    
    async def record_gateway_activity(self, gateway: str, results: List[Dict]):
        """Record gateway testing activity"""
        activity = {
            'timestamp': time.time(),
            'gateway': gateway,
            'cards_tested': len(results),
            'successful_checks': sum(1 for r in results if r.get('success', False)),
            'risk_level': self._calculate_risk_level(results)
        }
        
        self.activity_log.append(activity)
        self.logger.info(f"Recorded activity for {gateway}: {activity}")
    
    def _calculate_risk_level(self, results: List[Dict]) -> str:
        """Calculate risk level based on testing results"""
        success_rate = sum(1 for r in results if r.get('success', False)) / len(results)
        
        if success_rate > 0.8:
            return "HIGH"
        elif success_rate > 0.5:
            return "MEDIUM"
        else:
            return "LOW"
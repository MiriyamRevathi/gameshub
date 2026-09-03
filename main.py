"""
Main Entry Point for Python Games Enterprise Platform.
Supports Interactive CLI, Web Server Dispatch, and Headless Simulation.
"""
import sys
import os
import argparse

from core.math.vector import VectorMathEngine
from core.ai.minimax import MinimaxAgent
from core.engine.game_loop import GameLoopManager
from core.network.client import ClientHandler
from core.storage.database import DatabaseManager
from core.analytics.telemetry import TelemetryService
from core.simulation.simulator import SimulatorHarness
from services.auth_service import AuthService
from services.game_service import GameService
from api.routes import APIRouter
from cli.menu import TerminalMenu

def main() -> int:
    """Master CLI and Platform Bootstrapper."""
    parser = argparse.ArgumentParser(description="Enterprise Python Games Platform")
    parser.add_argument("--mode", choices=["cli", "web", "sim", "test"], default="cli", help="Operating mode")
    parser.add_argument("--game", type=str, default="chess", help="Target game")
    parser.add_argument("--port", type=int, default=5000, help="Web server port")
    args = parser.parse_args()

    print("=" * 60)
    print("   PYTHON GAMES ENTERPRISE MULTI-GAME PLATFORM v1.0.0")
    print("=" * 60)
    print(f"[*] Operating Mode: {args.mode}")
    print(f"[*] Target Game:    {args.game}")

    if args.mode == "cli":
        print("[+] Initializing Interactive CLI Menu...")
        menu = TerminalMenu()
        view = menu.render_cli_view_1({"status": "ready", "game": args.game})
        print(view)
        print("[+] CLI Session Initialized successfully.")
        return 0
    elif args.mode == "sim":
        print("[+] Running Headless Monte Carlo Simulation...")
        harness = SimulatorHarness()
        result = harness.run_simulation_scenario_1({"game": args.game}, max_iterations=100)
        print(f"[+] Simulation Result: {result}")
        return 0
    elif args.mode == "web":
        print(f"[+] Launching Flask Web Application on port {args.port}...")
        import app
        app.app.run(host="0.0.0.0", port=args.port, debug=False)
        return 0
    elif args.mode == "test":
        import pytest
        return pytest.main(["tests/"])
    return 0

if __name__ == "__main__":
    sys.exit(main())

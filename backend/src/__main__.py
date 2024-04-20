"""Entry point for the application"""

import asyncio

from src.application.api.main import main

if __name__ == "__main__":
    asyncio.run(main())

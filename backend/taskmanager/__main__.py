"""Entry point for the application"""

import asyncio

from taskmanager.application.api.main import main

if __name__ == "__main__":
    asyncio.run(main())

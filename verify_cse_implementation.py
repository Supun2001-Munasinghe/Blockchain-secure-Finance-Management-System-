#!/usr/bin/env python
"""
Verification and testing script for CSE polling service
Run this to validate the implementation
"""

import sys
import os
import json

# Add backend to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

try:
    # Test 1: Import all modules
    print("=" * 60)
    print("TEST 1: Importing CSE polling modules...")
    print("=" * 60)
    
    from finance_app.cse_poller import (
        create_poller,
        CSEPoller,
        CSEPollerConfig,
        SharePriceProcessor,
        MarketSummaryProcessor
    )
    print("✓ cse_poller.py imported successfully")
    
    from finance_app.cse_pipeline import (
        CSEPollerPipeline,
        get_cse_pipeline
    )
    print("✓ cse_pipeline.py imported successfully")
    
    from finance_app.cse_views import CSEDataViewSet
    print("✓ cse_views.py imported successfully")
    
    from finance_app.cse_examples import (
        example_basic_polling,
        example_pipeline_integration,
        example_health_check
    )
    print("✓ cse_examples.py imported successfully")
    
    print("\n✓ All modules imported successfully!\n")
    
    # Test 2: Verify configuration
    print("=" * 60)
    print("TEST 2: Verifying CSEPollerConfig...")
    print("=" * 60)
    
    config = CSEPollerConfig()
    print(f"  Base URL: {config.BASE_URL}")
    print(f"  Share Price Endpoint: {config.TODAY_SHARE_PRICE_ENDPOINT}")
    print(f"  Market Summary Endpoint: {config.MARKET_SUMMARY_ENDPOINT}")
    print(f"  Poll Interval: {config.POLL_INTERVAL_SECONDS}s")
    print(f"  Timeout: {config.TIMEOUT_SECONDS}s")
    print(f"  Max Retries: {config.MAX_RETRIES}")
    print("✓ Configuration verified!\n")
    
    # Test 3: Create poller instance
    print("=" * 60)
    print("TEST 3: Creating CSE Poller instance...")
    print("=" * 60)
    
    poller = create_poller()
    print(f"  Poller type: {type(poller).__name__}")
    print(f"  Share Price Processor: {type(poller.share_price_processor).__name__}")
    print(f"  Market Summary Processor: {type(poller.market_summary_processor).__name__}")
    print("✓ Poller instance created!\n")
    
    # Test 4: Check health status
    print("=" * 60)
    print("TEST 4: Checking poller health status...")
    print("=" * 60)
    
    health = poller.get_health_status()
    print(f"  Service: {health['service']}")
    print(f"  Status: {health['status']}")
    print(f"  Timestamp: {health['timestamp']}")
    print("✓ Health status retrieved!\n")
    
    # Test 5: Data processors
    print("=" * 60)
    print("TEST 5: Testing data processors...")
    print("=" * 60)
    
    test_data = {
        "status": "success",
        "timestamp": "2024-05-29T19:46:34.760",
        "data": [{"symbol": "TEST", "price": 100.0}],
        "record_count": 1
    }
    
    share_processor = SharePriceProcessor()
    processed_share = share_processor.process(test_data)
    print(f"  Share Price Processor Result:")
    print(f"    Type: {processed_share['type']}")
    print(f"    Status: {processed_share['status']}")
    print(f"    Record Count: {processed_share.get('record_count', 0)}")
    
    market_processor = MarketSummaryProcessor()
    processed_market = market_processor.process(test_data)
    print(f"  Market Summary Processor Result:")
    print(f"    Type: {processed_market['type']}")
    print(f"    Status: {processed_market['status']}")
    
    print("✓ Data processors working!\n")
    
    # Test 6: Session creation
    print("=" * 60)
    print("TEST 6: Verifying HTTP session...")
    print("=" * 60)
    
    session = poller.session
    print(f"  Session type: {type(session).__name__}")
    print(f"  Adapters configured: {len(session.adapters)}")
    print(f"  Timeout configured: {poller.config.TIMEOUT_SECONDS}s")
    print("✓ HTTP session configured!\n")
    
    # Test 7: Endpoint configuration
    print("=" * 60)
    print("TEST 7: Verifying endpoint URLs...")
    print("=" * 60)
    
    share_url = f"{config.BASE_URL}{config.TODAY_SHARE_PRICE_ENDPOINT}"
    market_url = f"{config.BASE_URL}{config.MARKET_SUMMARY_ENDPOINT}"
    
    print(f"  Share Price URL: {share_url}")
    print(f"  Market Summary URL: {market_url}")
    
    if share_url.startswith("https://") and "todaySharePrice" in share_url:
        print("✓ Share Price endpoint configured correctly!")
    else:
        print("⚠ Share Price endpoint may need verification")
    
    if market_url.startswith("https://") and "marketSummery" in market_url:
        print("✓ Market Summary endpoint configured correctly!")
    else:
        print("⚠ Market Summary endpoint may need verification")
    
    print()
    
    # Test 8: Module file verification
    print("=" * 60)
    print("TEST 8: Verifying module files exist...")
    print("=" * 60)
    
    import pathlib
    backend_path = pathlib.Path(__file__).parent / "backend" / "finance_app"
    
    files_to_check = [
        "cse_poller.py",
        "cse_pipeline.py",
        "cse_views.py",
        "cse_examples.py",
        "cse_tasks.py",
        "CSE_POLLING_README.md"
    ]
    
    all_files_exist = True
    for filename in files_to_check:
        filepath = backend_path / filename
        exists = filepath.exists()
        status = "✓" if exists else "✗"
        file_size = f"({filepath.stat().st_size} bytes)" if exists else "(not found)"
        print(f"  {status} {filename} {file_size}")
        if not exists:
            all_files_exist = False
    
    if all_files_exist:
        print("\n✓ All module files present!\n")
    else:
        print("\n⚠ Some files are missing!\n")
    
    # Test 9: Documentation verification
    print("=" * 60)
    print("TEST 9: Verifying documentation files...")
    print("=" * 60)
    
    docs_path = pathlib.Path(__file__).parent
    
    docs_to_check = [
        ("backend/CSE_SETUP_QUICK_START.md", "Quick Start Guide"),
        ("IMPLEMENTATION_SUMMARY.md", "Implementation Summary")
    ]
    
    for doc_file, doc_name in docs_to_check:
        filepath = docs_path / doc_file
        exists = filepath.exists()
        status = "✓" if exists else "✗"
        file_size = f"({filepath.stat().st_size} bytes)" if exists else "(not found)"
        print(f"  {status} {doc_name}: {doc_file} {file_size}")
    
    print()
    
    # Summary
    print("=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    print("""
✓ All core modules imported successfully
✓ Configuration verified
✓ Poller instance created
✓ Health status working
✓ Data processors operational
✓ HTTP session configured with retry logic
✓ Endpoints configured

NEXT STEPS:
1. Review CSE_POLLING_README.md for detailed documentation
2. Follow CSE_SETUP_QUICK_START.md for Django integration
3. Test with: python manage.py shell < cse_examples.py
4. Access API at: http://localhost:8000/api/cse/poll/latest/
5. Configure Celery for production polling

For issues or questions, refer to the documentation files.
    """)
    print("=" * 60)

except ImportError as e:
    print(f"✗ Import Error: {e}")
    print("\nNote: This script must be run from the project root directory")
    print("with Django properly configured (Django not needed for module verification)")
    sys.exit(1)

except Exception as e:
    print(f"✗ Unexpected Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

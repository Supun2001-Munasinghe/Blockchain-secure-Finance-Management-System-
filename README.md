# SecureAI Finance Smart System

A comprehensive full-stack financial system combining AI/ML, blockchain integration, and secure banking features for advanced financial analysis and cryptocurrency trading.

## 🚀 Features

- **AI-Powered Analysis**: LSTM neural networks for Bitcoin, Gold, and CSE market predictions
- **Real-time Data Processing**: Time-series analysis with 15m, 1h, 4h, 1d intervals
- **Blockchain Integration**: Ethereum smart contracts and wallet management
- **Banking Services**: User authentication, account management, transaction tracking
- **RESTful API**: Django REST Framework backend with comprehensive endpoints
- **Modern UI**: React frontend with Vite for fast development and production builds
- **Database Management**: SQLite with Django ORM and migrations

## 📋 Project Structure

```
SecureAI_Finance_Smart_system/
├── ai_models/              # LSTM models and training pipelines
│   ├── lstm_finance_model.py
│   ├── train_lstm_model.py
│   ├── analyze_lstm_results.py
│   └── dataset/            # Training data (BTC, Gold, CSE)
│       └── saved/          # Trained models (*.keras)
├── backend/                # Django application
│   ├── finance_app/        # Main app with AI integration
│   ├── blockchain/         # Blockchain utilities
│   ├── manage.py
│   ├── requirements.txt
│   └── db.sqlite3
├── frontend/               # React application (Vite)
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
└── blockchain/             # Smart contracts
    ├── FinanceToken.sol
    ├── FinanceToken_ABI.json
    └── wallet.py
```

## 🛠️ Tech Stack

### Backend
- Django 4.x
- Django REST Framework
- SQLite
- Python 3.8+

### Frontend
- React 18+
- Vite
- CSS/PostCSS
- ESLint

### AI/ML
- TensorFlow/Keras
- NumPy, Pandas
- Time-series forecasting with LSTM

### Blockchain
- Solidity (Smart Contracts)
- Ethereum Integration
- Web3.py

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm/yarn

### Backend Setup

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

4. Start Django server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start development server:
   ```bash
   npm run dev
   ```

### AI Models Setup

1. Navigate to ai_models directory:
   ```bash
   cd ai_models
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train models:
   ```bash
   python train_lstm_model.py
   ```

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration

### Banking
- `GET /api/bank/accounts/` - Get user accounts
- `POST /api/bank/transactions/` - Create transaction

### AI Predictions
- `GET /api/ai/forecast/bitcoin/` - Bitcoin price forecast
- `GET /api/ai/forecast/gold/` - Gold price forecast
- `GET /api/ai/forecast/cse/` - CSE market forecast

### Blockchain
- `GET /api/blockchain/wallet/` - Get wallet info
- `POST /api/blockchain/transaction/` - Create blockchain transaction

##  AI Models

### LSTM Finance Model
Predicts financial asset prices using Long Short-Term Memory networks:
- **Supported Assets**: Bitcoin, Gold, CSE stocks
- **Timeframes**: 15m, 1h, 4h, 1d
- **Input Features**: OHLCV (Open, High, Low, Close, Volume)
- **Output**: Price predictions with confidence intervals

##  Security Features

- Secure user authentication and authorization
- Database encryption for sensitive data
- API rate limiting
- CORS protection
- Smart contract audit ready

## 📚 Documentation

- [START_HERE.md](START_HERE.md) - Quick start guide
- [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) - Detailed implementation guide
- [LSTM_PREDICTION_GUIDE.md](backend/finance_app/LSTM_PREDICTION_GUIDE.md) - AI model documentation
- [CSE_POLLING_SERVICE.md](CSE_POLLING_SERVICE.md) - Real-time CSE data polling

## 🧪 Testing

Run backend tests:
```bash
cd backend
python manage.py test
```

Run frontend tests:
```bash
cd frontend
npm run test
```

## 🐳 Docker Deployment

Build and run with Docker Compose:
```bash
docker-compose up --build
```

## 📊 Performance Optimization

See [PERFORMANCE_OPTIMIZATION.md](PERFORMANCE_OPTIMIZATION.md) for:
- Database indexing strategies
- API caching mechanisms
- Model optimization techniques
- Frontend bundle optimization

## 🚨 Troubleshooting

- **AI Page Issues**: See [AI_PAGE_DEBUG_GUIDE.md](AI_PAGE_DEBUG_GUIDE.md)
- **CSE Service Issues**: See [CSE_POLLING_SERVICE.md](CSE_POLLING_SERVICE.md)
- **Implementation Issues**: See [IMPLEMENTATION_COMPLETE.md](IMPLEMENTATION_COMPLETE.md)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For issues and questions:
1. Check the documentation files in the root directory
2. Review the [walkthrough.md](walkthrough.md.resolved)
3. Check implementation guides

## 🎯 Project Status

✅ Core backend API development complete
✅ LSTM AI models trained and integrated
✅ Frontend React application functional
✅ Blockchain integration implemented
✅ CSE data polling service active
✅ Database migrations completed

## 🔄 Version History

- **v1.0.0** - Initial release with AI forecasting, banking, and blockchain features

---

**Made with ❤️ for Advanced Financial Technology**
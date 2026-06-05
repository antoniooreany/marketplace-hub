import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import './index.css';
import { ProductsPage } from './pages/ProductsPage';
import { BillingPage } from './pages/BillingPage';
import { WebhooksPage } from './pages/WebhooksPage';
import { DebugOpsPage } from './pages/DebugOpsPage';

const Layout = ({ children }: { children: React.ReactNode }) => (
  <div className="layout">
    <aside className="sidebar">
      <h3>Marketplace Hub</h3>
      <nav>
        <NavLink to="/" className="nav-item">Dashboard</NavLink>
        <NavLink to="/products" className="nav-item">Products</NavLink>
        <NavLink to="/integrations" className="nav-item">Integrations</NavLink>
        <NavLink to="/sync-jobs" className="nav-item">Sync Jobs</NavLink>
        <NavLink to="/webhooks" className="nav-item">Webhooks</NavLink>
        <NavLink to="/billing" className="nav-item">Billing</NavLink>
        <NavLink to="/debug-ops" className="nav-item">Debug & Ops</NavLink>
        <NavLink to="/settings" className="nav-item">Settings</NavLink>
      </nav>
    </aside>
    <main className="main-content">
      {children}
    </main>
  </div>
);

const Placeholder = ({ title }: { title: string }) => (
  <div>
    <h1>{title}</h1>
    <p>This is a placeholder for the {title} page. Implementation coming soon.</p>
  </div>
);

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Placeholder title="Dashboard" />} />
          <Route path="/products" element={<ProductsPage />} />
          <Route path="/integrations" element={<Placeholder title="Integrations" />} />
          <Route path="/sync-jobs" element={<Placeholder title="Sync Jobs" />} />
          <Route path="/webhooks" element={<WebhooksPage />} />
          <Route path="/billing" element={<BillingPage />} />
          <Route path="/debug-ops" element={<DebugOpsPage />} />
          <Route path="/settings" element={<Placeholder title="Settings" />} />
          <Route path="/login" element={<Placeholder title="Login" />} />
          <Route path="*" element={<Placeholder title="404 - Not Found" />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;

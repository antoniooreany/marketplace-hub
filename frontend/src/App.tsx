import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

export const App = () => {
  return (
    <BrowserRouter>
      <div className='flex h-screen'>
        <nav className='w-64 bg-gray-800 text-white p-4'>
          <Link to='/'>Dashboard</Link>
        </nav>
        <main className='flex-1 p-4'>
          <Routes>
            <Route path='/' element={<div>Dashboard</div>} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
};

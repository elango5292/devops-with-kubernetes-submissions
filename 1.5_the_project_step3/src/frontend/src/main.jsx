import { StrictMode, useState, useEffect } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, NavLink, Link } from 'react-router-dom'
import './index.css'

const Home = () => (
  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', flex: 1, textAlign: 'center', padding: '40px' }}>
    <h1 style={{ fontSize: '3rem', marginBottom: '20px' }}>🚀 Space Explorer</h1>
    <p style={{ fontSize: '1.2rem', color: '#94a3b8', marginBottom: '30px', maxWidth: '500px' }}>
      Discover the universe with NASA's Astronomy Picture of the Day
    </p>
    <Link to="/nasa" style={{ padding: '15px 40px', backgroundColor: '#6366f1', color: 'white', textDecoration: 'none', borderRadius: '8px', fontSize: '1.1rem' }}>
      View Today's Image →
    </Link>
  </div>
)

const Nasa = () => {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
      .then(res => res.json())
      .then(d => { setData(d); setLoading(false) })
  }, [])

  if (loading) return <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flex: 1, color: '#94a3b8' }}>Loading...</div>

  return (
    <div style={{ display: 'flex', flex: 1, gap: '30px', padding: '30px', overflow: 'auto' }}>
      <div style={{ flex: 2, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <img src={data.url} alt={data.title} style={{ maxWidth: '100%', maxHeight: '80vh', borderRadius: '12px', boxShadow: '0 10px 40px rgba(0,0,0,0.5)' }} />
      </div>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
        <span style={{ color: '#6366f1', fontSize: '14px', marginBottom: '10px' }}>{data.date}</span>
        <h2 style={{ fontSize: '1.8rem', marginBottom: '20px', lineHeight: 1.3 }}>{data.title}</h2>
        <p style={{ color: '#94a3b8', lineHeight: 1.7, fontSize: '15px' }}>{data.explanation}</p>
      </div>
    </div>
  )
}

function App() {
  const linkStyle = ({ isActive }) => ({
    padding: '12px 24px',
    textDecoration: 'none',
    color: isActive ? '#6366f1' : '#94a3b8',
    borderBottom: isActive ? '2px solid #6366f1' : '2px solid transparent'
  })

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#0f172a', color: '#f1f5f9', fontFamily: 'system-ui, sans-serif', display: 'flex', flexDirection: 'column' }}>
      <nav style={{ display: 'flex', gap: '10px', padding: '15px 30px', borderBottom: '1px solid #1e293b' }}>
        <NavLink to="/" style={linkStyle}>Home</NavLink>
        <NavLink to="/nasa" style={linkStyle}>NASA APOD</NavLink>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/nasa" element={<Nasa />} />
      </Routes>
    </div>
  )
}

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>
)

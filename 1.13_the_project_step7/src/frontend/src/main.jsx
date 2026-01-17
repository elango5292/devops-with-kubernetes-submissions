import { StrictMode, useState, useEffect } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, NavLink, Link } from 'react-router-dom'
import './index.css'

import TodoInput from './components/TodoInput'
import TodoList from './components/TodoList'

const Home = () => {
  const [isImageLoading, setIsImageLoading ] = useState(true)
  
  return (
  <div style={{ padding: '40px', maxWidth: '1200px', margin: '0 auto', width: '100%' }}>
    <h1 style={{ fontSize: '3rem', marginBottom: '40px', textAlign: 'center' }}>To-do</h1>
    
    <div style={{ 
      display: 'flex', 
      flexWrap: 'wrap', 
      gap: '40px', 
      alignItems: 'stretch', // ensures both columns have same height if possible, or use min-height
      justifyContent: 'center',
      minHeight: '60vh' // Ensure enough height for vertical centering
    }}>
      {/* Left Column: Image (Approx 45%) */}
      <div style={{ flex: '1 1 45%', minWidth: '300px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        {isImageLoading && <div className="loader"></div>}
        <img 
          src="/api/image" 
          alt="Daily Feature"
          onLoad={() => setIsImageLoading(false)}
          style={{ 
            width: '100%',
            height: 'auto',
            maxHeight: '70vh', // Prevent it from becoming excessively tall
            objectFit: 'cover', // or 'contain' depending on preference
            borderRadius: '12px',
            boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
            display: isImageLoading ? 'none' : 'block'
          }} 
        />
      </div>

      {/* Right Column: Todo App */}
      <div className="custom-scroll" style={{ 
        flex: '1 1 45%', 
        minWidth: '300px', 
        display: 'flex', 
        flexDirection: 'column', 
        alignItems: 'center',
        justifyContent: 'center', // Vertically center content
        maxHeight: '70vh', // Match image max height constraint
        overflowY: 'auto', // Scroll if content is too long
        padding: '20px'
      }}>
        <div style={{ width: '100%', maxWidth: '400px' }}> {/* Wrapper to keep input/list aligned */}
          <TodoInput />
          <TodoList />
        </div>
      </div>
    </div>
  </div> )
}

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
        <NavLink to="/" style={linkStyle}>To-Do</NavLink>
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

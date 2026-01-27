import { StrictMode, useState, useEffect } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route, NavLink, Link } from 'react-router-dom'
import './index.css'

import TodoInput from './components/TodoInput'
import TodoList from './components/TodoList'

const Home = () => {
  const [isImageLoading, setIsImageLoading ] = useState(true)
  const [todos, setTodos] = useState([])

  const fetchTodos = async () => {
    try {
      const response = await fetch('/api/todos')
      if (response.ok) {
        const data = await response.json()
        setTodos(data)
      }
    } catch (error) {
       console.error("Error fetching todos:", error)
    }
  }

  const handleAddTodo = async (todoText) => {
    try {
      const response = await fetch('/api/todos', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ todo: todoText }),
      })
      if (response.ok) {
        fetchTodos()
      }
    } catch (error) {
       console.error("Error adding todo:", error)
    }
  }

  const handleToggleTodo = async (id, done) => {
      try {
        const response = await fetch(`/api/todos/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ done: done })
        })
        if (response.ok) {
            fetchTodos()
        }
      } catch (error) {
          console.error("Error updating todo:", error)
      }
  }

  useEffect(() => {
    fetchTodos()
  }, [])

  const activeTodos = todos.filter(t => !t.done)
  const doneTodos = todos.filter(t => t.done)

  return (
  <div style={{ padding: '40px', maxWidth: '1200px', margin: '0 auto', width: '100%' }}>
    <h1 style={{ fontSize: '3rem', marginBottom: '40px', textAlign: 'center' }}>To-do</h1>

    {/* Top Section: Image and Active Todos */}
    <div style={{
      display: 'flex',
      flexWrap: 'wrap',
      gap: '40px',
      alignItems: 'stretch',
      justifyContent: 'center',
      minHeight: '60vh',
      marginBottom: '60px'
    }}>
      {/* Left Column: Image */}
      <div style={{ flex: '1 1 45%', minWidth: '300px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        {isImageLoading && <div className="loader"></div>}
        <img
          src="/api/image"
          alt="Daily Feature"
          onLoad={() => setIsImageLoading(false)}
          style={{
            width: '100%',
            height: 'auto',
            maxHeight: '70vh',
            objectFit: 'cover',
            borderRadius: '12px',
            boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
            display: isImageLoading ? 'none' : 'block'
          }}
        />
      </div>

      {/* Right Column: Todo App (Active Only) */}
      <div style={{
        flex: '1 1 45%',
        minWidth: '300px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '20px',
        backgroundColor: '#0f172a', // Match bg to hide scroll behind input if needed
        maxHeight: '70vh' // Constrain height
      }}>
        <div style={{ width: '100%', maxWidth: '400px', display: 'flex', flexDirection: 'column', height: '100%' }}>
            {/* Input Fixed at Top */}
            <div style={{ flexShrink: 0, marginBottom: '20px' }}>
                <TodoInput onAdd={handleAddTodo} />
            </div>

            {/* Scrollable List */}
            <div className="custom-scroll" style={{
                flexGrow: 1,
                overflowY: 'auto',
                paddingRight: '10px' // Space for scrollbar
            }}>
                <TodoList todos={activeTodos} onToggle={handleToggleTodo} />
            </div>
        </div>
      </div>
    </div>

    {/* Bottom Section: Done Todos Table */}
    <div style={{
        width: '100%',
        height: '100vh', // Full mac screen height
        overflowY: 'auto',
        backgroundColor: '#1e293b',
        borderRadius: '12px',
        padding: '20px'
    }}>
        <h2 style={{ marginBottom: '20px', borderBottom: '1px solid #334155', paddingBottom: '10px' }}>Completed Tasks</h2>
        <table style={{ width: '100%', borderCollapse: 'collapse', color: '#f1f5f9' }}>
            <thead>
                <tr style={{ borderBottom: '1px solid #334155', textAlign: 'left' }}>
                    <th style={{ padding: '15px' }}>Task</th>
                    <th style={{ padding: '15px', width: '150px' }}>Status</th>
                </tr>
            </thead>
            <tbody>
                {doneTodos.map(todo => (
                    <tr key={todo.id} style={{ borderBottom: '1px solid #334155' }}>
                        <td style={{ padding: '15px' }}>{todo.todo}</td>
                        <td style={{ padding: '15px' }}>
                            <span style={{
                                backgroundColor: '#10b981',
                                padding: '4px 8px',
                                borderRadius: '4px',
                                fontSize: '0.9rem',
                                color: 'white'
                            }}>Done</span>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
        {doneTodos.length === 0 && <p style={{ textAlign: 'center', marginTop: '30px', color: '#94a3b8' }}>No completed tasks yet.</p>}
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

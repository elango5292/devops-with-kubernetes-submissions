
const TodoInput = () => {
  return (
    <div style={{ display: 'flex', gap: '10px', marginTop: '20px', width: '100%', maxWidth: '400px' }}>
      <input 
        type="text" 
        maxLength={140} 
        placeholder="Enter a todo (max 140 chars)..." 
        style={{ 
          flex: 1, 
          padding: '10px', 
          borderRadius: '8px', 
          border: '1px solid #ccc',
          backgroundColor: '#1e293b',
          color: 'white'
        }}
      />
      <button 
        style={{ 
          padding: '10px 20px', 
          backgroundColor: '#6366f1', 
          color: 'white', 
          border: 'none', 
          borderRadius: '8px', 
          cursor: 'pointer',
          fontWeight: 'bold'
        }}
        onClick={() => alert('Todo added (placeholder)')}
      >
        Send
      </button>
    </div>
  )
}

export default TodoInput

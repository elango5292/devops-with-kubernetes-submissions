

const TodoList = ({ todos }) => {
  return (
    <div style={{ width: '100%', maxWidth: '400px', marginTop: '20px', textAlign: 'left' }}>
      <ul style={{ listStyleType: 'none', padding: 0 }}>
        {todos && todos.map((todo, index) => (
          <li key={index} style={{
            backgroundColor: '#1e293b',
            padding: '12px',
            marginBottom: '8px',
            borderRadius: '8px',
            borderLeft: '4px solid #6366f1'
          }}>
            {todo}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default TodoList

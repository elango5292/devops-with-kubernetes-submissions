

const TodoList = ({ todos, onToggle }) => {
  return (
    <div style={{ width: '100%', maxWidth: '400px', marginTop: '20px', textAlign: 'left' }}>
      <ul style={{ listStyleType: 'none', padding: 0 }}>
        {todos && todos.map((todo) => (
          <li key={todo.id} style={{
            backgroundColor: '#1e293b',
            padding: '12px',
            marginBottom: '8px',
            borderRadius: '8px',
            borderLeft: '4px solid #6366f1',
            wordWrap: 'break-word',
            overflowWrap: 'break-word',
            whiteSpace: 'pre-wrap',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center'
          }}>
            <span>{todo.todo}</span>
            <button
                onClick={() => onToggle(todo.id, !todo.done)}
                style={{
                    backgroundColor: '#10b981',
                    color: 'white',
                    border: 'none',
                    borderRadius: '4px',
                    padding: '4px 8px',
                    cursor: 'pointer',
                    fontSize: '0.8rem'
                }}
            >
                Done
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default TodoList

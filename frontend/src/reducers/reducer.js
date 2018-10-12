import { 
	ADD_TODO, 
	UPDATE_TODO, 
	DELETE_TODO, 
	GET_TODOS 
} from '../actions/actions'

const initialState = {
	todos:[],
	currentTodo: null
}

export const todoApp = (state = initialState, action) => {
	switch (action.type) {
		case ADD_TODO:
			return Object.assign({}, state, {
				todos: [
					...state.todos,
					{
						title: action.data.title,
						description: action.data.description,
						completed: action.data.completed,
						todolistid: action.data.todolistid
					}
				]
			})
		case GET_TODOS:
			console.log(action)
			return Object.assign({}, state, {
				todos: action.data
			})
		default:
			return state
	}
}

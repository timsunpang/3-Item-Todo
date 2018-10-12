import { APIUtilFetchTodos, APIUtilCreateTodo, APIUtilEditTodo, APIUtilDeleteTodo } from '../util/apiUtil'

export const ADD_TODO = 'ADD_TODO'
export const UPDATE_TODO = 'UPDATE_TODO'
export const DELETE_TODO = 'DELETE_TODO'
export const GET_TODOS = 'GET_TODOS'

export const addTodo = (data) => ({
	type: ADD_TODO,
	data
})

export const updateTodo = (data) => ({
	type: UPDATE_TODO,
	data
})

export const deleteTodo = (id) => ({
	type: DELETE_TODO,
	id
})

export const getTodos = () => (dispatch) => {
	return APIUtilFetchTodos()
		.then(response => response.json(), error => console.log('An error occurred: ', error))
		.then(data => dispatch(	
			{
				type: GET_TODOS,
				data
			}
		)
	)
}

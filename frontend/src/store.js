import { createStore, applyMiddleware } from 'redux'
import { todoApp } from './reducers/reducer'
import thunk from 'redux-thunk';

export const store = createStore(
	todoApp, 
	applyMiddleware(thunk)
)
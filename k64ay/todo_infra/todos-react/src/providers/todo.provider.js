import React, { createContext, useContext, useEffect, useReducer } from 'react';

import api from '../utils/api';

const SET_TODOS = 'SET_TODOS';
const SET_FETCHING = 'SET_FETCHING';
const UPDATE_TODO = 'UPDATE_TODO';

let initialState = {
    isFetching: true,
    page: 1,
    ordering: null,
    showComplete: false,
    count: 0,
    has_next: false,
    has_prev: false,
    results: [],
};

export const todoReducer = (state, action) => {
    switch (action.type) {
        case SET_FETCHING: {
            const isFetching = action.payload;
            return {...state, isFetching};
        }
        case SET_TODOS: {
            return {...state, ...action.payload, isFetching: false};
        }
        case UPDATE_TODO: {
            const updatedTodo = action.payload;
            const results = state.results.map(item => {
                if (item.id === updatedTodo.id) {
                    return {...item, ...updatedTodo};
                }
                return item;
            })
            return {...state, results};
        }
        
        default:
            return state;
    }
};

export const TodoContext = createContext({
    ...initialState,
    addTodo: (todo) => {},
    updateTodo: (updatedTodo) => {},
    deleteTodo: (todoId) => {},
    nextPage: () => {},
    prevPage: () => {},
    toggleShowComplete: () => {},
    switchOrder: (order) => {},
});

export function useTodoContext() {
   return useContext(TodoContext);
}

const TodoProvider = (props) => {
    const [state, dispatch] = useReducer(todoReducer, initialState);

    const addTodo = async (desc) => {
        await api.post('/tasks/', {
            desc: desc,
            done: false
        });
        loadTodos();
    };

    const deleteTodo = async (id) => {
        await api.delete(`/tasks/${id}/`);
        loadTodos();
    };

    const updateTodo = async (updatedTodo) => {
        await api.put(`/tasks/${updatedTodo.id}/`, updatedTodo);

        dispatch({ type: UPDATE_TODO, payload: updateTodo });
    };

    const toggleShowComplete = async () => {
        loadTodos({showComplete: !state.showComplete});
    }

    const switchOrder = (ordering) => {
        loadTodos({ordering});
    }

    const loadTodos = async ({page, showComplete, ordering}={}) => {
        const pageNo = page || state.page;
        const newShowComplete = showComplete !== undefined ? showComplete : state.showComplete;
        const newOrdering = ordering || state.ordering;
        let queryParams = {page: pageNo};

        if (!newShowComplete) {
            queryParams.done = false;
        }

        if (newOrdering) {
            queryParams.ordering = newOrdering;
        }

        dispatch({ type: SET_FETCHING, payload: true });
        const { data } = await api.get(`/tasks/`, {
            params: queryParams
        });
        dispatch({ type: SET_TODOS, payload: {
            ...data, 
            page: pageNo, 
            showComplete: newShowComplete,
            ordering: newOrdering,
        }});
    };

    const nextPage = async () => {
        const newPage = state.page + 1;
        await loadTodos({page: newPage});
    };

    const prevPage = async () => {
        const newPage = state.page - 1;
        await loadTodos({page: newPage});
    };

    useEffect(() => {
        loadTodos();
    }, []);

    return (
        <TodoContext.Provider 
            value={{ ...state, 
                dispatch, 
                addTodo, 
                updateTodo, 
                deleteTodo,
                nextPage,
                prevPage,
                toggleShowComplete,
                switchOrder,
            }}
            {...props}
        />
    );
};

export default TodoProvider;

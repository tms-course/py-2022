import React, { Suspense } from 'react';

import styles from './TodoContainer.module.scss';
import TodoProvider from '../providers/todo.provider';
import TodoDashboard from '../components/TodoDashboard';

const TodoContainer = () => {

    return (
        <TodoProvider>
            <Suspense fallback={<h1>Loading todos...</h1>}>
                <div className={styles.container}>
                    <div className="inner">
                        <TodoDashboard />
                    </div>
                </div>
            </Suspense>
        </TodoProvider>
    );
};

export default TodoContainer;

import { useEffect, useState } from 'react';
import { apiFetch } from '../api/api';

export const ProductsPage = () => {
    const [products, setProducts] = useState([]);
    useEffect(() => {
        apiFetch('/products/').then(setProducts);
    }, []);
    return (
        <div>
            <h1>Products</h1>
            <ul>{products.map((p: any) => <li key={p.id}>{p.title} - {p.sku}</li>)}</ul>
        </div>
    );
};

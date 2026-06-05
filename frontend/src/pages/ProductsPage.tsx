import { useEffect, useState } from 'react';
import { apiFetch } from '../api/api';

export const ProductsPage = () => {
    const [products, setProducts] = useState([]);
    useEffect(() => {
        // Based on current route: /api/v1/products/
        // Base is /api/v1
        // Endpoint passed is /products/
        // Result: /api/v1/products/
        apiFetch<any[]>('/products/').then(setProducts);
    }, []);
    return (
        <div>
            <h1>Products</h1>
            <ul>{products.map((p: any) => <li key={p.id}>{p.title} - {p.sku}</li>)}</ul>
        </div>
    );
};

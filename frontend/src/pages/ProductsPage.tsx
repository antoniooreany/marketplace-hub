import { useEffect, useState } from 'react';
import { apiFetch } from '../api/api';

export const ProductsPage = () => {
    const [products, setProducts] = useState<any[]>([]);
    useEffect(() => {
        // Based on current route: /api/v1/products/
        // API now returns { content: [...] }
        apiFetch<{ content: any[] }>('/products/').then(data => setProducts(data.content));
    }, []);
    return (
        <div>
            <h1>Products</h1>
            <ul>{products.map((p: any) => <li key={p.id}>{p.title} - {p.sku}</li>)}</ul>
        </div>
    );
};

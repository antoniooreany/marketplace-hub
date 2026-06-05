import { API_BASE_URL } from './client';

export const apiFetch = async <T>(endpoint: string, options?: RequestInit): Promise<T> => {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        ...options,
        headers: { 'Content-Type': 'application/json', ...options?.headers }
    });
    if (!response.ok) throw new Error('API request failed');
    return response.json();
};

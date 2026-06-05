import { render, screen, waitFor } from '@testing-library/react';
import { ProductsPage } from '../../pages/ProductsPage';
import { vi, test, expect } from 'vitest';
import * as api from '../../api/api';

vi.mock('../../api/api', () => ({
  apiFetch: vi.fn(),
}));

test('renders products', async () => {
  vi.mocked(api.apiFetch).mockResolvedValue({ content: [{ id: 1, title: 'Test Product', sku: 'SKU1' }] });
  
  render(<ProductsPage />);
  await waitFor(() => {
    expect(screen.getByText(/Test Product/i)).toBeDefined();
  });
});

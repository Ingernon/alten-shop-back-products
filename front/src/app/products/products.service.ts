import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Product } from './product.class';

@Injectable({
  providedIn: 'root'
})

export class ProductsService {

    private static productslist: Product[] = null;
    private products$: BehaviorSubject<Product[]> = new BehaviorSubject<Product[]>([]);

    constructor(private http: HttpClient) { }

    getProducts(): Observable<Product[]> {
        if( ! ProductsService.productslist )
        {
            this.http.get<any>("http://localhost:3000/products").subscribe(data => {
                ProductsService.productslist = data;
                    
                this.products$.next(ProductsService.productslist);
            });
        }
        else
        {
            this.products$.next(ProductsService.productslist);
        }

        return this.products$;
    }

    create(prod: Product): Observable<Product[]> {
        console.log(prod)
        this.http.post<any>("http://localhost:3000/products/", prod).subscribe(data => {
            ProductsService.productslist.push(data);
            this.products$.next(ProductsService.productslist);
        });
        
        return this.products$;
    }

    update(prod: Product): Observable<Product[]>{
        this.http.patch<any>("http://localhost:3000/products/"+prod.id, prod).subscribe(data => {
            ProductsService.productslist.forEach(element => {
                if(element.id == data.id)
                {
                    element.name = data.name;
                    element.category = data.category;
                    element.code = data.code;
                    element.description = data.description;
                    element.image = data.image;
                    element.inventoryStatus = data.inventoryStatus;
                    element.price = data.price;
                    element.quantity = data.quantity;
                    element.rating = data.rating;
                }
            });
            this.products$.next(ProductsService.productslist);
        });

        return this.products$;
    }


    delete(id: number): Observable<Product[]>{
        this.http.delete<any>("http://localhost:3000/products/"+id).subscribe(_ => {
            ProductsService.productslist = ProductsService.productslist.filter(value => { return value.id !== id } );
            this.products$.next(ProductsService.productslist);
        });
        
        return this.products$;
    }
}
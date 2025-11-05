import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TxtToSrt } from './txt-to-srt';

describe('TxtToSrt', () => {
  let component: TxtToSrt;
  let fixture: ComponentFixture<TxtToSrt>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TxtToSrt]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TxtToSrt);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

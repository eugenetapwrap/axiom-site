// Тексты главной на языке текущей страницы (ветка intl)
import * as ru from './home';
import * as en from './home.en';
import { isEn } from '../lib/i18n';

export const content = () => (isEn() ? en : ru) as typeof ru;

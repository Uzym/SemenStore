import './globals.scss'
import type { Metadata } from 'next'
import Providers from '@/providers/Providers'
import { roboto } from '@/theme/fonts'
import MainLayout from '@/components/layouts/MainLayout'

export const metadata: Metadata = {
	title: 'UStore',
	description: 'Магазин одежды и обуви',
}

export default function RootLayout({
	children,
}: {
	children: React.ReactNode
}) {
	return (
		<html lang='ru'>
			<Providers>
				<body className={roboto.className}>
					<MainLayout />
					<main>{children}</main>
				</body>
			</Providers>
		</html>
	)
}
